import requests
import json

def dbleu_postservercount(apikey, servercount):

    r = requests.patch('https://api.discord-botlist.eu/v1/update', headers={
        "Authorization": f"Bearer {apikey}"
                }, json=({"serverCount": servercount}))


    if r.status_code == 400:

        return print("[API] discord-botlist.eu HTTP: 400 - Please check your API key. Access denied. - ./update")
    

    if r.status_code == 200:

        return print(f"[API] discord-botlist.eu HTTP: 200 - Posted server count ({servercount}) - ./update")

    else:
        content = r.content
        content = content.decode("utf-8")


        content = json.loads(content)


        return print(f"[API] discord-botlist.eu HTTP: {r.status_code} - {content['message']} - ./update")
    


def dbleu_getbotvotes(apikey):

    r = requests.get('https://api.discord-botlist.eu/v1/votes', headers={"Authorization": f"Bearer {apikey}"})

    if r.status_code == 400:

        return print("[API] discord-botlist.eu HTTP: 400 - Please check your API key. Access denied. - ./votes")

    if r.status_code == 200:

        print(f"[API] discord-botlist.eu HTTP: {r.status_code} - ./votes")

        return r

    else:

        content = r.content
        content = content.decode("utf-8")

        content = json.loads(content)

        return print(f"[API] discord-botlist.eu HTTP: {r.status_code} - {content['message']} - ./votes")



def dbleu_getbotdata(apikey):

    r = requests.get('https://api.discord-botlist.eu/v1/ping', headers={"Authorization": f"Bearer {apikey}"})

    if r.status_code == 400:

        return print("[API] discord-botlist.eu HTTP: 400 - Please check your API key. Access denied. - ./ping")

    if r.status_code == 200:

        print(f"[API] discord-botlist.eu HTTP: {r.status_code} - ./ping")

        return r

    else:
        
        content = r.content
        content = content.decode("utf-8")

        content = json.loads(content)

        return print(f"[API] discord-botlist.eu HTTP: {r.status_code} - {content['message']} - ./ping")

