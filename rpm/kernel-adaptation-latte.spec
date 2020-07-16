# Device details
%define device latte

# Kernel target architecture
%define kernel_arch x86

# Crossbuild toolchain to use
#define crossbuild aarch64

# RPM target architecture, remove to leave it unaffected
# You should have a good reason to change the target architecture
# (like building on aarch64 targeting an armv7hl repository)
%define device_target_cpu i486

# Defconfig to pick-up
%define defconfig ct_defconfig

# Build modules
%define build_modules 1

# Build Image
#define build_Image 1

# Build uImage
##define build_uImage 1

# Build zImage
%define build_zImage 1

# Build and pick-up the following devicetrees
#define devicetrees allwinner/sun50i-a64-pinephone-1.0.dtb allwinner/sun50i-a64-pinephone-1.1.dtb allwinner/sun50i-a64-pinephone-1.2.dtb allwinner/sun50i-a64-pinetab.dtb allwinner/sun50i-a64-dontbeevil.dtb

%include kernel-adaptation-simplified/kernel-adaptation-simplified.inc
