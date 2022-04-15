import os
from nextcord.ext import commands

client = commands.Bot(command_prefix = ['*', 'bob '])

# heroku why u no work?

# EVENTS
@client.event
async def on_ready():
    print(f'I\'m online as {client.user.name}')

# COMMANDS
@client.command('test')
async def test(ctx):
    await ctx.send('bob test')

client.run(os.environ['CLIENT_TOKEN'])