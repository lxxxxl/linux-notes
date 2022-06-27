# Contents
- [Uninstall Google Services from Android](#uninstall-google-services-from-android)
- [Yandex TV factory reset](#yandex-tv-factory-reset)
- [Kernel compilation](#kernel-compilation)
- [Cross compilation](#cross-compilation)


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


## Kernel compilation

### Kernel
```bash
# get toolchain
mkdir workdir && cd workdir
CLANGVER=clang-r365631c
ANDROIDBRANCH=android-11.0.0_r28
mkdir $CLANGVER && cd $CLANGVER
wget https://android.googlesource.com/platform/prebuilts/clang/host/linux-x86/+archive/$ANDROIDBRANCH/$CLANGVER.tar.gz
tar -xzf $CLANGVER.tar.gz && cd ..
git clone \
    -b $ANDROIDBRANCH \
    --single-branch https://android.googlesource.com/platform/prebuilts/gcc/linux-x86/aarch64/aarch64-linux-android-4.9

# get and build kernel sources
git clone https://github.com/OnePlusOSS/android_kernel_oneplus_sm8250.git kernelsource
cd kernelsource
export ARCH=arm64
export CLANG_TRIPLE=aarch64-linux-gnu-
export CROSS_COMPILE=aarch64-linux-androidkernel-
export LINUX_GCC_CROSS_COMPILE_PREBUILTS_BIN=$(pwd)/../aarch64-linux-android-4.9/bin
export CLANG_PREBUILT_BIN=$(pwd)/../$CLANGVER/bin
BUILDPARAMS="CC=clang LD=ld.lld EXTRA_CMDS='' STOP_SHIP_TRACEPRINTK=1"
export PATH=$PATH:$LINUX_GCC_CROSS_COMPILE_PREBUILTS_BIN:$CLANG_PREBUILT_BIN

make $BUILDPARAMS mrproper
```

### Separate module
```bash
make -C <path_to_kernel_src> M=$PWD
```

## Cross compilation
### NDK
```bash
/path/to/ndk/ndk-build NDK_PROJECT_PATH=. APP_BUILD_SCRIPT=./Android.mk APP_PLATFORM=android-16
```
### Configure script
```bash
CROSS_COMPILE=/path/to/toolchain/bin/arm-linux-androideabi- CC=/path/to/toolchain/bin/arm-linux-androideabi-clang ./configure --host=aarch64-linux-android- 
```
