import discord
from datetime import datetime
from discord.ext import tasks


from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    
    TOKEN = "DISCORD_BOT_TOKEN" #トークン
    CHANNEL_ID = "803619260349677589" #チャンネルID
    # 接続に必要なオブジェクトを生成
    client = discord.Client()
    
    
    await ctx.send('pong')


bot.run(token)
