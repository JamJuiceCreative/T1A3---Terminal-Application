#!/bin/bash

if which python3 >/dev/null; then
    echo Awesome! You have python on your system!
else 
    sudo apt-get install python3
fi

source venv/bin/activate

if python -c 'import pkgutil; exit(not pkgutil.find_loader("colored"))'; then
    echo 'colored found'
else
    pip3 install colored
fi

if python -c 'import pkgutil; exit(not pkgutil.find_loader("art"))'; then
    echo 'art found'
else
    pip3 install art
fi

python3 game_menu.py









python3 game_menu.py

