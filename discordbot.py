from discord.ext import commands
import os
import traceback
import asyncio
import discord
import random

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

intents = discord.Intents.default()  # デフォルトのIntentsオブジェクトを生成
intents.typing = False  # typingを受け取らないように
bot = commands.Bot(command_prefix = '/', intents = intents)


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def d(ctx):
    num_random = random.randrange(1,6)
    await ctx.send(str(ctx.author)+"さんのダイスの結果は")
    await ctx.send(str(num_random))

@bot.command()
async def n(ctx):
    await ctx.send(str(ctx.author.id))
    await ctx.send(str(ctx.author))


@bot.command()
async def vote(ctx, title, *select):
  if len(select) > 10:
    err = discord.Embed(title = "選択肢が多すぎます。", color = discord.Colour.red())
    await ctx.send(embed = err)
    return

  emoji_list = ["1⃣", "2⃣", "3⃣", "4⃣", "5⃣", "6⃣", "7⃣", "8⃣", "9⃣", "🔟"]
  embed = discord.Embed(title = title, color = discord.Colour.red())

  for num in range(len(select)):
    embed.add_field(name = emoji_list[num], value = select[num], inline = False)
  msg = await ctx.send(embed = embed)

  for i in range(len(select)):
    await msg.add_reaction(emoji_list[i])
  return

@bot.event
async def on_ready():
  activity = discord.Activity(name = '/vote', type = discord.ActivityType.playing)
  await bot.change_presence(activity = activity)

if __name__ == "__main__":




bot.run(token)






