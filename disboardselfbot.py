import discord
import discord
import aiohttp
from discord.ext import commands
from discord.ext.commands import has_role
from discord.ext.commands import bot

import time

client = discord.Client()

bot_token = "NTQ0MTU3MzE5MDQ3Njc1OTE2.Xk2low.OttNSRqiX6nq6oRn-9SDb0KIvi8"

bot = commands.Bot(command_prefix="$")
bot.session = aiohttp.ClientSession(loop=bot.loop)

@bot.event

async def on_message(message):
    if message.content.find("$start") != -1:
        if message.author.id == 603408199000784898:
            channel = await bot.fetch_channel("677643356997943348")
            _loop = False
            while _loop == False:
                await channel.send("!d bump")
                time.sleep(7200)
        else:
            channel = await bot.fetch_channel("677643356997943348")
            await channel.send("hx#7774")

    if message.content.find("$stop") != -1:
        if message.author.id == 603408199000784898:
            _loop = True
        else:
            pass





if __name__ =="__main__":
    bot.run(bot_token, bot=False)