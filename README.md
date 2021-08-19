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
  
## GRUB 2.0 boot from ISO file
This is example for Ubuntu distro. Other distros would have another kernel paths and options.   
```bash
menuentry "ISO boot" {
   insmod part_msdos
   insmod ntfs
   set isofile="/ubuntu.iso"
   loopback loop (hd1,msdos1)$isofile
   linux (loop)/casper/vmlinuz boot=casper iso-scan/filename=$isofile noprompt noeject
   initrd (loop)/casper/initrd
}
```
  
## LXQT Run apps without prompt
You can disable it in `PCmanfm > preferences > Launch executable files without prompt`  
[Link](https://github.com/lxqt/lxqt/issues/1523#issuecomment-406578815)
  
## Mouse wheel adjust sound volume instead of page scrolling
Hold DPI button of mouse for 5 seconds.  
  
## 404  Not Found while performing apt-get update
Problem occurs when your distro lifecycle come to it's end.  
In `/etc/apt/sources.list` replace all occurencies of `archive.ubuntu.com` with `old-releases.ubuntu.com`  
[Link](https://www.digitalocean.com/community/questions/i-cannot-update-from-19-04-to-19-10-no-longer-has-a-release-file)
  
## Copy-Paste to Ubuntu Linux VM
If you are using VMWare Player with `Ubuntu Linux` to enable _copy-paste_ functionality from _host to VM_ you should install `open-vm-tools-desktop` package:
```bash
sudo apt install open-vm-tools
```

## Uninstall Google Services from Android
```bash
pm list packages | grep google
```
> package:com.google.android.youtube  
> package:com.google.android.configupdater  
> package:com.google.android.setupwizard  
> package:com.google.android.packageinstaller  
> package:com.google.android.gms  
> package:com.google.android.tts  
> package:com.google.android.partnersetup  
> package:com.google.android.feedback  
> package:com.google.android.gsf.login  
```bash
pm path com.google.android.gms
```
> package:/system/priv-app/PrebuiltGmsCore/PrebuiltGmsCore.apk  
```bash
mount -o remount,rw /system
rm /system/priv-app/PrebuiltGmsCore/PrebuiltGmsCore.apk
reboot
```

## A stop job is running for Session c2 of user
A workaround to this problem is to reduce this timeout in `/etc/systemd/system.conf` down from 90s to for example 10s:
```
DefaultTimeoutStopSec=10s
```
and run the following command in terminal after making changes
```
$ systemctl daemon-reload
```
[Link](https://unix.stackexchange.com/a/297318)
