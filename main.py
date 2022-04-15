import os
from nextcord.ext import commands

client = commands.Bot(command_prefix = ['*', 'bob '])

# heroku why u no work?

# EVENTS
@client.event
async def on_ready():
    print(f'I\'m online as {client.user.name}')

# Handling errors
@client.event
async def on_command_error(ctx, error):
    # No perms?
    if isinstance(error, commands.MissingPermissions):
        await ctx.reply(f'Nice try, {ctx.author.mention}\nYou\'ll need perms for that to work.')
    else:
        await ctx.reply(f':thinking: Hmm... something went wrong.\nThis is the error I got: `{error}`')

# COMMANDS
@client.command('test', help = 'Just for testing, nothing special')
async def test(ctx):
    await ctx.reply('if you\'re seeing this, something probably went right')

@client.command('permtest', help = 'testing perms')
@commands.has_permissions(administrator = True)
async def permtest(ctx):
    await ctx.reply('it worked :triumph:')

client.run(os.environ['CLIENT_TOKEN'])