#!/bin/sh

echo Removing torpinger file
sudo rm /etc/network/if-up.d/torpinger
echo Removing zetproxy file 
sudo rm /etc/network/if-up.d/zetproxy
echo Removing phelp file
sudo rm /usr/bin/phelp


echo Uninstallation complete
