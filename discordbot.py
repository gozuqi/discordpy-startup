from discord.ext import commands
import os
import traceback
import asyncio
import discord
import random

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def judge(ctx):
    await ctx.send('1')

@client.event
async def on_message(message):
    if message.content.startswith("!dice"): #command
        if client.user != message.author:
            num_random = random.randrange(1,6)
            m = str(num_random)
            await client.send_message(message.channel, m)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')







bot.run(token)
