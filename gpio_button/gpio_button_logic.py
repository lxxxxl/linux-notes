#!/usr/bin/python
import os, time, select

GPIO_MODE_PATH= os.path.normpath('/sys/class/gpio/gpio199/direction')
GPIO_PIN_PATH=os.path.normpath('/sys/class/gpio/gpio199/value')
GPIO_EDGE_PATH=os.path.normpath('/sys/class/gpio/gpio199/edge')


file = open(GPIO_MODE_PATH, 'r+') 
file.write("in")          ## make the pin an input
file.close()                  

file = open(GPIO_EDGE_PATH, 'r+')
file.write("rising")          ## let the interrupt be triggered on rising and falling edges
file.close()                 

file = open(GPIO_PIN_PATH, 'r') ## open the virtual file

epoll = select.epoll()
epoll.register(file, select.EPOLLIN|select.EPOLLET) #register poll method and triggered events
while True:
    events = epoll.poll() #this line reads blocking
    for fileno, event in events:
        if fileno == file.fileno(): #check if interrupt comes from our handle
            print('Interrupt') 


file.close()  ## Make sure to close the file when you're done!