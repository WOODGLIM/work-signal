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
    
    
    
    await ctx.send('pong')
    
    
    


@tasks.loop(seconds=60)
    async def loop():
    # 現在の時刻
    now = datetime.now(JST).strftime('%H:%M')
    if now == '17:27':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('おはよう')  

    
    
    #ループ処理実行
    loop.start()
    
    # Botの起動とDiscordサーバーへの接続
    client.run(TOKEN)

    
        bot.run(token)
