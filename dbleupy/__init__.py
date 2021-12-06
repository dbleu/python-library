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


def dbleu_postservercount(apikey=None, servercount=None, log_disable=None):


    if apikey == None and servercount == None:
        if log_disable == None or log_disable == False:
            print(bcolors.FAIL + "[API] discord-botlist.eu HTTP: APIKEY & ServerCount missing find more on https://pypi.org/project/dbleupy/ - ./dbleu_postservercount" + bcolors.ENDC)
        return

    if apikey == None:
        if log_disable == None or log_disable == False:
            print(bcolors.FAIL + "[API] discord-botlist.eu HTTP: APIKEY missing find more on https://pypi.org/project/dbleupy/" + bcolors.ENDC)
        return

    if servercount == None:
        if log_disable == None or log_disable == False:
            print(bcolors.FAIL + "[API] discord-botlist.eu HTTP: ServerCount missing find more on https://pypi.org/project/dbleupy/" + bcolors.ENDC)
        return

    try:
        guilds = len(servercount.guilds)

        r = requests.patch('https://api.discord-botlist.eu/v1/update', headers={
            "Authorization": f"Bearer {apikey}"
                    }, json=({"serverCount": guilds}))


        if r.status_code == 400:
            if log_disable == None or log_disable == False:
                print(bcolors.FAIL + "[API] discord-botlist.eu HTTP: 400 - Please check your API key. Access denied." + bcolors.ENDC)
            return

        if r.status_code == 200:
            if log_disable == None or log_disable == False:

                print(bcolors.OKGREEN + f"[API] discord-botlist.eu HTTP: 200 - Posted server count ({guilds})" + bcolors.ENDC)
            return

        else:
            content = r.content
            content = content.decode("utf-8")


            content = json.loads(content)

            if log_disable == None or log_disable == False:
                print(bcolors.FAIL + f"[API] discord-botlist.eu HTTP: {r.status_code} - {content['message']}" + bcolors.ENDC)
            return
    except:
        if log_disable == None or log_disable == False:
            print(bcolors.FAIL + f"[API] discord-botlist.eu HTTP: Please check your bot's data (bot or self.bot)" + bcolors.ENDC)
        return


def dbleu_getbotvotes(apikey=None, log_disable=None):
    
    if apikey == None:
        if log_disable == None or log_disable == False:
            print(bcolors.FAIL + "[API] discord-botlist.eu HTTP: APIKEY missing find more on https://pypi.org/project/dbleupy/" + bcolors.ENDC)

        return

    r = requests.get('https://api.discord-botlist.eu/v1/votes', headers={"Authorization": f"Bearer {apikey}"})

    if r.status_code == 400:
        if log_disable == None or log_disable == False:
            print(bcolors.FAIL + "[API] discord-botlist.eu HTTP: 400 - Please check your API key. Access denied." + bcolors.ENDC)
        return

    if r.status_code == 200:

        print(bcolors.OKGREEN + f"[API] discord-botlist.eu HTTP: {r.status_code}" + bcolors.ENDC)

        return r

    else:

        content = r.content
        content = content.decode("utf-8")

        content = json.loads(content)

        if log_disable == None or log_disable == False:
            print(bcolors.FAIL + f"[API] discord-botlist.eu HTTP: {r.status_code} - {content['message']}" + bcolors.ENDC)
        return



def dbleu_getbotdata(apikey=None, log_disable=None):

    if apikey == None:
        if log_disable == None or log_disable == False:
            print(bcolors.FAIL + "[API] discord-botlist.eu HTTP: APIKEY missing find more on https://pypi.org/project/dbleupy/" + bcolors.ENDC)
        return


    r = requests.get('https://api.discord-botlist.eu/v1/ping', headers={"Authorization": f"Bearer {apikey}"})

    if r.status_code == 400:
        if log_disable == None or log_disable == False:
            print(bcolors.FAIL + "[API] discord-botlist.eu HTTP: 400 - Please check your API key. Access denied." + bcolors.ENDC)
        return

    if r.status_code == 200:

        print(bcolors.OKGREEN + f"[API] discord-botlist.eu HTTP: {r.status_code}" + bcolors.ENDC)

        return r

    else:
        
        content = r.content
        content = content.decode("utf-8")

        content = json.loads(content)
        if log_disable == None or log_disable == False:
            print(bcolors.FAIL + f"[API] discord-botlist.eu HTTP: {r.status_code} - {content['message']}" + bcolors.ENDC)
        return

