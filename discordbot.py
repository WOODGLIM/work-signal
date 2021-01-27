from discord.ext import commands
import os
import traceback
from datetime import datetime, timedelta, timezone

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def wk(ctx):
    JST = timezone(timedelta(hours=+9), 'JST') 
    now = datetime.now(JST).strftime('%H:%M')
    ms = ctx.author.name + "　[" + now + "]"    
    await ctx.send(ms)


bot.run(token)
