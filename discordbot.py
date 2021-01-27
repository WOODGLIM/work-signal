from discord.ext import commands
import os
import traceback
from datetime import datetime, timedelta, timezone
#ループのおまじない
import discord
from discord.ext import tasks

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
#チャンネル指定
CHANNEL_ID = "803619260349677589"

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def wk(ctx):
    JST = timezone(timedelta(hours=+9), 'JST')      
    now = datetime.now(JST)
    we = now.isoweekday()
    
    if we != 0 and we!= 6:
       youbi = datetime.now(JST).strftime('%A')
       ms = youbi + " 仕事だよー"
       await ctx.send(ms)


bot.run(token)
