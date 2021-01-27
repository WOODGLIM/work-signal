import discord
import datetime

client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']


@client.event
async def on_ready():
    print('時報機が起動しました。')

@client.event
async def on_message(message):
    
    date = datetime.datetime.now()
    hour = date.hour
    min = date.minute
    
        if message.author.bot:
           return
        if message.content == '何時？':
            await message.channel.send(str(hour) + '時です。')
        if message.content == '何分？':
             await message.channel.send(str(min) + '分です。')
        if message.content == '何時何分？':
             await message.channel.send(str(hour) + '時' + str(min) + '分です。')

client.run(token)
