dbleupy
==========


This package offers you a more user friendly and easier way to interact with the discord-botlist.eu HTTP api.


Installing
----------

**Python 3.4 or higher is required** - In the example py-cord was used, but other libs can be used as well.

To install the library you can just run the following command:

    pip install dbleupy


Quick Example (belongs in the on_ready event)
--------------
    from dbleupy import dbleu_postservercount, dbleu_getbotvotes, dbleu_getbotdata

    dbleuKEY = "APIKEY" # Get it from https://dev.discord-botlist.eu

    r = dbleu_getbotvotes(dbleuKEY, log_disable=False/True)
    print(r.content)
    # GET ALL BOT VOTES

    r = dbleu_getbotdata(dbleuKEY, log_disable=False/True)
    print(r.content)
    # GET BOTDATA

    dbleu_postservercount(dbleuKEY, bot/self.bot)
    # POST SERVERCOUNT 
    # IMPORTANT: The second parameter must be the discord.ext.commands.bot.Bot object


Example with auto post
~~~~~~~~~~~~~
from dbleupy import dbleu_postservercount, dbleu_getbotvotes, dbleu_getbotdata
from discord.ext import tasks

dbleuKEY = "APIKEY" # Get it from https://dev.discord-botlist.eu

r = dbleu_getbotvotes(dbleuKEY, log_disable=False/True)
print(r.content)
# GET ALL BOT VOTES

r = dbleu_getbotdata(dbleuKEY, log_disable=False/True)
print(r.content)
# GET BOTDATA

@tasks.loop(minutes=5)
async def auto_post():
    dbleu_postservercount(dbleuKEY, bot/self.bot, log_disable=False/True)
    # IMPORTANT: The second parameter must be the discord.ext.commands.bot.Bot object

auto_post.start()
# POST SERVERCOUNT every 5 mins.

~~~~~~~~~~~~~

Links
==========

Documentation: https://docs.discord-botlist.eu

Official Website: https://discord-botlist.eu

Official Discord Server: https://discord.gg/FR3cA5dWK6

Discord-botlist.eu Developers: https://dev.discord-botlist.eu