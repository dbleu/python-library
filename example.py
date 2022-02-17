import discord # USING py-cord
from dbleupy import dbleu_postservercount, dbleu_getbotvotes, dbleu_getbotdata
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=commands.when_mentioned_or("-"), intents=intents)

dbleuKEY = "" # Get it from https://dev.discord-botlist.eu

@bot.event
async def on_ready():
    auto_post.start()
    
    print(f"Online as {bot.user.name}")
    
    r = dbleu_getbotvotes(dbleuKEY, log_disable=False)
    print(r.content)

    r = dbleu_getbotdata(dbleuKEY, log_disable=False)
    print(r.content)


@tasks.loop(minutes=5)
async def auto_post():
    dbleu_postservercount(dbleuKEY, bot, log_disable=False)
    # IMPORTANT: The second parameter must be the discord.ext.commands.bot.Bot object


bot.run("DISCORD-BOT-TOKEN")
