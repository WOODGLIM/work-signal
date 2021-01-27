import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    asyncio.ensure_future(greeting_gm())

async def greeting_gm():
    await client.send_message(channel, 'おはよう')
    await asyncio.sleep(10)

client.run(token)
