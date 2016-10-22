#!/bin/sh

chmod +x ./zetproxy
chmod +x ./update.sh
chmod +x ./proxyhelper.py
chmod +x ./torpinger
#chmod +x ./auto-update.sh
chmod +x ./uninstall.sh

# Remove earlier installations if they exist
# Needs for people with earlier version of PH
# Which might clash
if [ -x "$(command -v /usr/bin/phelp)" ]
then 
    sudo rm /usr/bin/phelp
    echo Removing old phelp code
fi
if [ -x "$(command -v /usr/bin/zetproxy)" ]
then
    sudo rm /usr/bin/zetproxy
    echo Removing old zetproxy
fi
if [ -x "$(command -v /usr/bin/torpinger)" ]
then 
    sudo rm /usr/bin/torpinger
    echo Removing old torpinger
fi
if [ -x "$(command -v /etc/network/if-up.d/zetproxy)" ]
then
    sudo rm /etc/network/if-up.d/zetproxy
    echo Removing outdated zetproxy
fi
if [ -x "$(command -v /etc/network/if-up.d/torpinger)" ]
then 
    sudo rm /etc/network/if-up.d/torpinger
    echo Removing outdated torpinger
fi

DIR_PATH=/usr/share/proxyhelper 

if [ -x "$(command -v $DIR_PATH/install.sh)" ]
then 
    sudo rm -rf /usr/share/proxyhelper
    echo Removing all old source files
fi

# symlinks fail if the path is not absolute
sudo mkdir $DIR_PATH
echo Creating source directory /usr/share/proxyhelper
sudo cp ./proxyhelper.py ./update.sh ./zetproxy ./zettorproxy ./torpinger ./README.md ./install.sh ./uninstall.sh ./surely_parallel.py $DIR_PATH
echo Copying src files to directory
echo Creating symlinks
sudo ln -s $DIR_PATH/proxyhelper.py /usr/bin/phelp
sudo ln -s $DIR_PATH/zetproxy /etc/network/if-up.d/
sudo ln -s $DIR_PATH/torpinger /etc/network/if-up.d/
echo ===============================
echo ""
echo Installation complete
