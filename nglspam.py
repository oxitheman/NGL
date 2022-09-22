import json
import random
import time
from concurrent.futures import ThreadPoolExecutor
from msg import randomQuestions
try:
    import colorama
    import httpx
except:
    print('Please install colorama by doing pip3 install colorama or pip3 install httpx')
    exit()
errored = 0
sent = 0

def main(username, message, deviceid, proxy, proxystatus):
    global errored
    global sent
    green = '['+colorama.Fore.GREEN + colorama.Style.BRIGHT + '+' + colorama.Style.RESET_ALL + '] '
    red = '['+colorama.Fore.RED + colorama.Style.BRIGHT + '-' + colorama.Style.RESET_ALL + '] ' 
    yellow = '['+colorama.Fore.YELLOW + colorama.Style.BRIGHT + '!' + colorama.Style.RESET_ALL + '] ' 
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Accept-Language':'en-US,en;q=0.5', 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8', 'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:104.0) Gecko/20100101 Firefox/104.0'}

    with httpx.Client(headers=headers) as client:
        if proxystatus == True:
            client.proxies = {'http://': proxy}

        else:
            pass
        
        try: 
            
            postresp = client.post(f"https://ngl.link/{username}", data={'question': message + 'TROLLEDLOL ' + message, 'deviceId':deviceid})
            if postresp.status_code == 302:
                sent += 1
                print(green + f"Sent {message} to victim, Sent {sent} messages, Errored {errored} messages")
                
            elif postresp.status_code == 404:
                print(red + f"User {username} does not exist")
                exit()
            elif postresp.status_code == 429:
                print(red + f"User {username} is rate limited")
                
                
        except Exception as e:
            errored+=1
            print(yellow + f'Error: {e}')
            main(username, messages(), deviceid(), proxy())
def messages():
    return random.choice(randomQuestions)
def proxy():
    return 'http://' + random.choice(list(open('proxy.txt')))
def deviceid():
    return ''.join(random.choice('0123456789abcdefghijklmnopqrstuvwxyz-') for i in range(36))

question = '[' + colorama.Fore.YELLOW + '?' + colorama.Back.YELLOW + colorama.Style.BRIGHT + colorama.Style.RESET_ALL + '] '
info = question = '[' + colorama.Fore.YELLOW + '!' + colorama.Back.YELLOW + colorama.Style.BRIGHT + colorama.Style.RESET_ALL + '] '
print(colorama.Fore.LIGHTRED_EX + '''
▒█▄░▒█ ▒█▀▀█ ▒█░░░ 　 ▒█▀▀▀█ ▒█▀▀█ ░█▀▀█ ▒█▀▄▀█ 
▒█▒█▒█ ▒█░▄▄ ▒█░░░ 　 ░▀▀▀▄▄ ▒█▄▄█ ▒█▄▄█ ▒█▒█▒█ 
▒█░░▀█ ▒█▄▄█ ▒█▄▄█ 　 ▒█▄▄▄█ ▒█░░░ ▒█░▒█ ▒█░░▒█
''' + colorama.Fore.GREEN + 'Made by https://github.com/oxitheman' +  '\nStar the repository on github if you like it!' + colorama.Style.RESET_ALL)

print(colorama.Fore.GREEN  + colorama.Style.RESET_ALL)
print(info + 'If you would like to send random questions or use proxies edit config.json to true.')
username = str(input( question +"Enter username: "))
threadcount = int(input(question+"Enter thread count: "))
with open('config.json') as config:
    data = json.load(config)
    proxystatus = data['proxy']
    messagestatus = data['random_messages']
    delay = data['delay']
if messagestatus == True:
    with ThreadPoolExecutor(max_workers=threadcount) as executor:
        for x in range(threadcount):
            executor.submit(main, username, messages(), deviceid(), proxy(), proxystatus)
else:
    message = str(input(question+"Enter message: "))
    with ThreadPoolExecutor(max_workers=threadcount) as executor:
        for x in range(threadcount):
            executor.submit(main, username, message, deviceid(), proxy(), proxystatus)
            time.sleep(delay)




print(info + f'Sent {sent} messages to {username}.')