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
  
## GRUB 2.0 reboot to Windows once
Save the `~/.bashrc` file with new `reboot-to-windows` function:
```bash
function reboot-to-windows {
    WINDOWS_TITLE=`grep -i "^menuentry 'Windows" /boot/grub/grub.cfg|head -n 1|cut -d"'" -f2`
    sudo grub-reboot "$WINDOWS_TITLE"
    sudo reboot
}
```
[Link](https://askubuntu.com/questions/1014467/is-there-a-way-for-grub-to-automatically-reboot-into-windows-from-windows)  
It can also be wrapped with dialog box:
```bash
kdialog --warningyesno "Reboot to Windows?"
if [ $? = 0 ]; then
        reboot-to-windows
fi
```