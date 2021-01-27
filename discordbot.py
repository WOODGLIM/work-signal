#ループのおまじない
import discord
from datetime import datetime 
from discord.ext import tasks

token = os.environ['DISCORD_BOT_TOKEN']
#チャンネル指定
CHANNEL_ID = "803619260349677589"
# 接続に必要なオブジェクトを生成
client = discord.Client()

# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now(JST).strftime('%H:%M')
    if now == '17:16':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('おはよう')
#ループ処理実行
loop.start()
    
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
