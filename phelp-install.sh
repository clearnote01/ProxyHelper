#!/bin/bash

home=$HOME

if [ ! $(pwd | sed 's/\/.*\/.*\///') = '.proxyhelper' ]
then
    echo Exiting. This script should be run from "~/.proxyhelper" directory
    exit
fi

sudo chmod +x $home/.proxyhelper/proxyhelper.py
if [ -x "$(command -v phelp)" ] 
then 
    sudo rm /usr/bin/phelp
fi
sudo ln -s $home/.proxyhelper/proxyhelper.py /usr/bin/phelp

