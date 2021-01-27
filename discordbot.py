import time
import asyncio
from discord.ext import commands
import os
import traceback
import discord
from discord.ext import tasks
import asyncio
from datetime import datetime, timedelta, timezone

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID = 803967523954360363

# 接続に必要なオブジェクトを生成
client = discord.Client()


@client.event
async def on_ready():
    while True:
        channel = client.get_channel(CHANNEL_ID)

        # JP時間
        JST = timezone(timedelta(hours=+9), 'JST') 
        now = datetime.now(JST).strftime('%H:%M')

        if now == '08:00':

            await channel.send('　開始')

        if now == '12:00':

            await channel.send('　お昼')
            
        if now == '17:00':

            await channel.send('　終わり')
            
        if now == '22:00':

            await channel.send('　寝る時間')


        time.sleep(60)
client.run(token)
