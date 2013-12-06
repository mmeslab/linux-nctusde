#!/bin/sh

# make ARCH=arm xilinx_zynq_defconfig

export PATH=/home/michael/zedboard/u-boot-xlnx/tools:$PATH
make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- LOADADDR=0x00008000 uImage modules
make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- INSTALL_MOD_PATH=/tmp/ modules_install
