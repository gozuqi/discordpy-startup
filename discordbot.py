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
async def j(ctx):
    num_random = random.randrange(1,6)
    await ctx.send(str(num_random))

@bot.command()
async def n(ctx):
    guild = message.guild
    role = discord.utils.get(guild.roles, name="名前")
    await ctx.send(role)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


# 返信する非同期関数を定義
@client.event
async def reply(message):
    reply = f'{message.author.mention} ウェイヨー' # 返信メッセージの作成
    await message.channel.send(reply) # 返信メッセージを送信

# 発言時に実行されるイベントハンドラを定義
@client.event
async def on_message(message):
    if client.user in message.mentions: # 話しかけられたかの判定
        await reply(message) # 返信する非同期関数を実





bot.run(token)
