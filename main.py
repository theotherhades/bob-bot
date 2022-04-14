import os
from nextcord.ext import commands

client = commands.Bot(command_prefix = ['*', 'bob '])

# EVENTS
@client.event
async def on_ready():
    print(f'yeah whatever I\'m online as {client.user.name}')

# COMMANDS
@client.command('test')
async def test(ctx):
    await ctx.send('hi, hope you\'re doing ok.')

client.run(os.environ['CLIENT_TOKEN'])