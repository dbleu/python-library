from dbleupy import dbleu_postservercount, dbleu_getbotvotes, dbleu_getbotdata
from discord.ext import tasks

dbleuKEY = "APIKEY" # Get it from https://dev.discord-botlist.eu

r = dbleu_getbotvotes(dbleuKEY)
# GET ALL BOT VOTES


r = dbleu_getbotdata(dbleuKEY)
# GET BOTDATA


dbleu_postservercount(dbleuKEY, len(client/bot.guilds))
# POST SERVER COUNT


# YOU CAN FIND MORE ON https://docs.discord-botlist.eu





