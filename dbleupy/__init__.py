import requests
import json

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def dbleu_postservercount(apikey, servercount):

    r = requests.patch('https://api.discord-botlist.eu/v1/update', headers={
        "Authorization": f"Bearer {apikey}"
                }, json=({"serverCount": servercount}))


    if r.status_code == 400:

        return print(bcolors.FAIL + "[API] discord-botlist.eu HTTP: 400 - Please check your API key. Access denied. - ./update")
    

    if r.status_code == 200:

        return print(bcolors.OKGREEN + f"[API] discord-botlist.eu HTTP: 200 - Posted server count ({servercount}) - ./update")


    else:
        content = r.content
        content = content.decode("utf-8")


        content = json.loads(content)


        return print(bcolors.FAIL + f"[API] discord-botlist.eu HTTP: {r.status_code} - {content['message']} - ./update")
    


def dbleu_getbotvotes(apikey):

    r = requests.get('https://api.discord-botlist.eu/v1/votes', headers={"Authorization": f"Bearer {apikey}"})

    if r.status_code == 400:

        return print(bcolors.FAIL + "[API] discord-botlist.eu HTTP: 400 - Please check your API key. Access denied. - ./votes")

    if r.status_code == 200:

        print(bcolors.OKGREEN + f"[API] discord-botlist.eu HTTP: {r.status_code} - ./votes")

        return r

    else:

        content = r.content
        content = content.decode("utf-8")

        content = json.loads(content)

        return print(bcolors.FAIL + f"[API] discord-botlist.eu HTTP: {r.status_code} - {content['message']} - ./votes")



def dbleu_getbotdata(apikey):

    r = requests.get('https://api.discord-botlist.eu/v1/ping', headers={"Authorization": f"Bearer {apikey}"})

    if r.status_code == 400:

        return print(bcolors.FAIL + "[API] discord-botlist.eu HTTP: 400 - Please check your API key. Access denied. - ./ping")

    if r.status_code == 200:

        print(bcolors.OKGREEN + f"[API] discord-botlist.eu HTTP: {r.status_code} - ./ping")

        return r

    else:
        
        content = r.content
        content = content.decode("utf-8")

        content = json.loads(content)

        return print(bcolors.FAIL + f"[API] discord-botlist.eu HTTP: {r.status_code} - {content['message']} - ./ping")

