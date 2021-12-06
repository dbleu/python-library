import discord # USING py-cord
from dbleupy import dbleu_postservercount, dbleu_getbotvotes, dbleu_getbotdata
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=commands.when_mentioned_or("-"), intents=intents)


@bot.event
async def on_ready():
    print(f"Online as {bot.user.name}")

    dbleuKEY = "" # Get it from https://dev.discord-botlist.eu

    dbleu_postservercount(dbleuKEY, bot, log_disable=False)




bot.run("DISCORD-BOT-TOKEN")