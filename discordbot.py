from discord.ext import commands
import os
import traceback
import asyncio
import discord
import random

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_command_error(message, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await message.send(error_msg)


@bot.command()
async def d(message):
    num_random = random.randrange(1,6)
    await message.send(str(message.author) + "さんのダイスの結果は" + str(num_random)+ "です" )

@bot.command()
async def vote(message):
    q = await message.channel.send("勝者は？")
    [await q.add_reaction(i) for i in ('先行', '後攻')]  # for文の内包表記






bot.run(token)






