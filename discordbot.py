#ループのおまじない
import discord
from discord.ext import tasks
from datetime import datetime 

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
#チャンネル指定
CHANNEL_ID = "803619260349677589"


# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now(JST).strftime('%H:%M')
    if now == '17:05':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('おはよう')
#ループ処理実行
loop.start()
    
    

bot.run(token)
