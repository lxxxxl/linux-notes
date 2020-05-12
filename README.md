# Linux notes
My useful Linux tips and tricks  

## Gave up waiting for suspend/resume device
Problem occurs after SWAP partition removal.  
Fix:  
1. Remove SWAP partition info from _/etc/default/grub_  
2. Run __sudo update-grub__  
3. Run __sudo update-initramfs -u -k all__  
4. Reboot  
[Link](https://debianforum.ru/index.php?topic=13665.0)
