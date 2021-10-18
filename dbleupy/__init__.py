import requests
import json

from requests import api

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


def dbleu_postservercount(apikey=None, servercount=None):


    if apikey == None and servercount == None:
        return print(bcolors.FAIL + "[API] discord-botlist.eu HTTP: APIKEY & ServerCount missing find more on https://pypi.org/project/dbleupy/ - ./dbleu_postservercount" + bcolors.ENDC)


    if apikey == None:
        return print(bcolors.FAIL + "[API] discord-botlist.eu HTTP: APIKEY missing find more on https://pypi.org/project/dbleupy/ - ./dbleu_postservercount" + bcolors.ENDC)


    if servercount == None:
        return print(bcolors.FAIL + "[API] discord-botlist.eu HTTP: ServerCount missing find more on https://pypi.org/project/dbleupy/ - ./dbleu_postservercount" + bcolors.ENDC)


    r = requests.patch('https://api.discord-botlist.eu/v1/update', headers={
        "Authorization": f"Bearer {apikey}"
                }, json=({"serverCount": servercount}))


    if r.status_code == 400:

        return print(bcolors.FAIL + "[API] discord-botlist.eu HTTP: 400 - Please check your API key. Access denied. - ./dbleu_postservercount" + bcolors.ENDC)


    if r.status_code == 200:


        return print(bcolors.OKGREEN + f"[API] discord-botlist.eu HTTP: 200 - Posted server count ({servercount}) - ./dbleu_postservercount" + bcolors.ENDC)


    else:
        content = r.content
        content = content.decode("utf-8")


        content = json.loads(content)


        return print(bcolors.FAIL + f"[API] discord-botlist.eu HTTP: {r.status_code} - {content['message']} - ./dbleu_postservercount" + bcolors.ENDC)
    


def dbleu_getbotvotes(apikey=None):
    
    if apikey == None:
        return print(bcolors.FAIL + "[API] discord-botlist.eu HTTP: APIKEY missing find more on https://pypi.org/project/dbleupy/ - ./dbleu_getbotvotes" + bcolors.ENDC)

    r = requests.get('https://api.discord-botlist.eu/v1/votes', headers={"Authorization": f"Bearer {apikey}"})

    if r.status_code == 400:

        return print(bcolors.FAIL + "[API] discord-botlist.eu HTTP: 400 - Please check your API key. Access denied. - ./dbleu_getbotvotes" + bcolors.ENDC)

    if r.status_code == 200:

        print(bcolors.OKGREEN + f"[API] discord-botlist.eu HTTP: {r.status_code} - ./dbleu_getbotvotes" + bcolors.ENDC)

        return r

    else:

        content = r.content
        content = content.decode("utf-8")

        content = json.loads(content)

        return print(bcolors.FAIL + f"[API] discord-botlist.eu HTTP: {r.status_code} - {content['message']} - ./dbleu_getbotvotes" + bcolors.ENDC)



def dbleu_getbotdata(apikey=None):

    if apikey == None:
        return print(bcolors.FAIL + "[API] discord-botlist.eu HTTP: APIKEY missing find more on https://pypi.org/project/dbleupy/ - ./dbleu_getbotdata" + bcolors.ENDC)


    r = requests.get('https://api.discord-botlist.eu/v1/ping', headers={"Authorization": f"Bearer {apikey}"})

    if r.status_code == 400:

        return print(bcolors.FAIL + "[API] discord-botlist.eu HTTP: 400 - Please check your API key. Access denied. - ./dbleu_getbotdata" + bcolors.ENDC)

    if r.status_code == 200:

        print(bcolors.OKGREEN + f"[API] discord-botlist.eu HTTP: {r.status_code} - ./dbleu_getbotdata" + bcolors.ENDC)

        return r

    else:
        
        content = r.content
        content = content.decode("utf-8")

        content = json.loads(content)

        return print(bcolors.FAIL + f"[API] discord-botlist.eu HTTP: {r.status_code} - {content['message']} - ./dbleu_getbotdata" + bcolors.ENDC)

