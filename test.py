from dbleupy import dbleu_postservercount, dbleu_getbotvotes, dbleu_getbotdata
from discord.ext import tasks

dbleuKEY = "nCkpQMu95OYOdGGY7RJfBrf3KKWl7qWYBPytlR92wDgnzKrc6V"

r = dbleu_getbotvotes(dbleuKEY)
print(r.content)
# GET ALL BOT VOTES

r = dbleu_getbotdata(dbleuKEY)
print(r.content)
# GET BOTDATA



dbleu_postservercount(dbleuKEY, 2000)

#auto_post.start()





