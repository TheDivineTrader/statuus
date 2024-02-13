import requests, random, httpx, os, time
global infotoken                                           # .gg/avix

infotoken = 'https://discord.com/api/v9/users/@me'                                           # .gg/avix

thebios = []
                                           # .gg/avix
cookiemonster = httpx.get('https://discord.com/register').headers['set-cookie']
sep = cookiemonster.split(";")
sx = sep[0]
sx2 = sx.split("=")
dfc = sx2[1]                                           # .gg/avix
split = sep[6]
split2 = split.split(",")                                           # .gg/avix
split3 = split2[1]
split4 = split3.split("=")                                           # .gg/avix
sdc = split4[1]

with open('messages.txt','r', encoding='utf-8') as bios:
    for line in bios:
        thebios.append(line)
                                           # .gg/avix
bio_index = 0

def getBio():
    global bio_index
    if bio_index >= len(thebios):                                           # .gg/avix
        bio_index = 0
    bio = thebios[bio_index]
    bio_index += 1                                           # .gg/avix
    return bio

def headers(tokan):
    header = {                                           # .gg/avix
        "authority": "discord.com",
        "method": "POST",
        "path": "/api/v9/users/@me",
        "scheme": "https",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US",                                           # .gg/avix
        "Authorization": f"{tokan}",
        "content-length": "0",
        "cookie": f'__dcfduid={dfc}; __sdcfduid={sdc}',                                           # .gg/avix
        "origin": "https://discord.com",
        'referer': 'https://discord.com/channels/@me',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": 'Mozilla/5.0 (Windows NT 6.1; rv:40.0) Gecko/20100101 Firefox/40.0',
        "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
        "x-debug-options": "bugReporterEnabled",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
    }
    return header                                           # .gg/avix
while True:
    os.system('cls' if os.name=='nt' else 'clear')
    global tukan

    tukan = input('Input Token: ')
    r = requests.get('https://discordapp.com/api/v9/users/@me/library', headers = headers(tukan))
    if r.status_code != 200:
        print('Invalid Token')
        time.sleep(1)                                           # .gg/avix
    else:
        break                                           # .gg/avix

def login():
    reqinfo = requests.get(infotoken, headers=headers(tukan))                                           # .gg/avix

    return f'@{reqinfo.json()["username"]}'

def main(delay, mode):
    statusurl = 'https://discord.com/api/v9/users/@me/settings'
    os.system('cls' if os.name=='nt' else 'clear')                                           # .gg/avix
    print(f'- Logged In As {login()}')
    os.system('pause')                                           # .gg/avix

    if mode == 'random':                                           # .gg/avix
        while True:
            payload = {
                'custom_status': {'text': random.choice(thebios)}                                           # .gg/avix
            }
            applybio = requests.patch(statusurl, headers=headers(tukan), json=payload)
            time.sleep(delay)
    elif mode == 'order':                                           # .gg/avix
        bio_index = 0
        while True:
            if bio_index >= len(thebios):                                           # .gg/avix
                bio_index = 0
            payload = {                                           # .gg/avix
                'custom_status': {'text': thebios[bio_index]}                                           # .gg/avix
            }
            applybio = requests.patch(statusurl, headers=headers(tukan), json=payload)
            bio_index += 1
            time.sleep(delay)
    else:                                           # .gg/avix
        print("Invalid Mode\nPlease choose either [ Random ] or [ Order ]")
        return

choice = input('Mode: [ Random / Order ]: ').lower()                                           # .gg/avix

delay1 = float(input('Delay: '))                                           # .gg/avix

if __name__ == '__main__':                                           # .gg/avix
    mode = choice
    main(delay1, mode)                                           # .gg/avix

