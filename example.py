from dbleupy import dbleu_postservercount, dbleu_getbotvotes, dbleu_getbotdata
from discord.ext import tasks

dbleuKEY = "APIKEY"

r = dbleu_getbotvotes(dbleuKEY)
print(r.content)
# GET ALL BOT VOTES

r = dbleu_getbotdata(dbleuKEY)
print(r.content)
# GET BOTDATA



dbleu_postservercount(dbleuKEY, len(client/bot.guilds))

#auto_post.start()





