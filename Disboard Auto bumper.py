import discord
from discord.ext import tasks
from discord.ext import commands
client=commands.Bot(command_prefix = '.', self_bot=True)

a=input('What is your token?:\n')
b=input('What is channel ID you want to bump in?:\n')

@tasks.loop(seconds=7210)
async def bumping():
    channel = await client.fetch_channel(b)
    await channel.send('!d bump')
    print('Bumped, next bump in 7200 seconds.')

@client.event
async def on_ready():
    bumping.start()

client.run(a, bot=False)

