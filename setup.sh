#!/bin/zsh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" && brew install python@3.11 && pip3 install requests bs4 lxml && chmod +x /start.sh
chmod +x ~/SchoolCheatTools/SchoolCheatTools.sh
cd ~
sh_dir=$HOME
sh_dir+=/SchoolCheatTools/SchoolCheatTools.sh
echo $sh_dir
osascript -e "tell application \"System Events\" to make new login item at end with properties {path:\"$sh_dir\"}"
