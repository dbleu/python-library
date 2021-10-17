dbleupy
==========


This package offers you a more user friendly and easier way to interact with the discord-botlist.eu HTTP api.


Installing
----------

**Python 3.4 or higher is required - If you want to use auto_post, you must have discord.ext**

To install the library you can just run the following command:


    # Linux/macOS
    python3 -m pip install -U dbleupy

    # Windows
    py -3 -m pip install -U dbleupy


Quick Example
--------------
    from dbleupy import dbleu_postservercount, dbleu_getbotvotes, dbleu_getbotdata

    dbleuKEY = "APIKEY" # Get it from https://dev.discord-botlist.eu

    r = dbleu_getbotvotes(dbleuKEY)
    print(r.content)
    # GET ALL BOT VOTES

    r = dbleu_getbotdata(dbleuKEY)
    print(r.content)
    # GET BOTDATA

    dbleu_postservercount(dbleuKEY, len(client/bot.guilds))
    # POST SERVERCOUNT


Example with auto post
~~~~~~~~~~~~~
from dbleupy import dbleu_postservercount, dbleu_getbotvotes, dbleu_getbotdata
from discord.ext import tasks

dbleuKEY = "APIKEY" # Get it from https://dev.discord-botlist.eu

r = dbleu_getbotvotes(dbleuKEY)
print(r.content)
# GET ALL BOT VOTES

r = dbleu_getbotdata(dbleuKEY)
print(r.content)
# GET BOTDATA

@tasks.loop(minutes=5)
async def auto_post():
    dbleu_postservercount(dbleuKEY, len(client/bot.guilds))

auto_post.start()
# POST SERVERCOUNT every 5 mins.

~~~~~~~~~~~~~

Links
==========

Documentation: https://docs.discord-botlist.eu

Official Website: https://discord-botlist.eu

Official Discord Server: https://discord.gg/FR3cA5dWK6

Discord-botlist.eu Developers: https://dev.discord-botlist.eu