#!/bin/zsh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" && brew install python@3.11 && pip3 install requests bs4 lxml && chmod +x /start.sh