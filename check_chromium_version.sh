#!/bin/sh
mkdir -p ./opera-stable-$1
pushd ./opera-stable-$1 &> /dev/null
echo -en "\033[0;35m    Downloading Opera Stable package:\033[0m\n"
wget -N -q --show-progress ftp://ftp.opera.com/pub/opera/desktop/$1/linux/opera-stable_$1_amd64.deb
echo -en "\033[0;35m    Opera Stable package hash:\033[0m\n"
echo -en "\033[0;32m$(md5sum opera-stable_$1_amd64.deb)\033[0m\n"
ar p opera-stable_$1_amd64.deb data.tar.xz | tar -xJf-
CHROMIUM_VER=$(strings ./usr/lib/x86_64-linux-gnu/opera/opera | grep Chrome/ | cut --delimiter=/ --fields=2)
echo -en "\033[0;35m    Chromium version:\033[0m\n"
echo -en "\033[0;32m$(echo $CHROMIUM_VER)\033[0m\n"
echo -en "\033[0;35m    Downloading Chromium sources archive:\033[0m\n"
wget -N -q --show-progress https://commondatastorage.googleapis.com/chromium-browser-official/chromium-$CHROMIUM_VER.tar.xz
echo -en "\033[0;35m    Chromium sources archive hash:\033[0m\n"
echo -en "\033[0;32m$(md5sum chromium-$CHROMIUM_VER.tar.xz)\033[0m\n"
popd &> /dev/null
exit 0
