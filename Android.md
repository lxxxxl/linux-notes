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

## Yandex TV factory reset
1. Unplug TV from AC input
2. Press and hold Power On OR Channel+ button on TV
3. Power on TV while holding button
4. Hold button 20 seconds more while factory reset screen apperas

