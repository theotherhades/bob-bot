import os
import json
import random
import requests
import nextcord
from nextcord.ext import commands

client = commands.Bot(command_prefix = ['*', 'bob '])

# CONSTANTS
EMBED_COLORS = [nextcord.Color.red(), nextcord.Color.yellow(), nextcord.Color.blurple()]

# GLOBALS
url = 'https://bob-bot-db.theotherhades-alt.repl.co/'

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
        await ctx.reply(f':smiling_imp: Nice try, {ctx.author.mention}\nYou\'ll need perms for that to work.')
    else:
        await ctx.reply(f':thinking: Hmm... something went wrong.\nThis is the error I got: `{error}`')
        print('Received error: ' + str(error))



# COMMANDS
@client.command('test', help = 'Just for testing, nothing special')
async def test(ctx):
    await ctx.reply('if you\'re seeing this, something probably went right')

@client.command('permtest', help = 'testing perms')
@commands.has_permissions(administrator = True)
async def permtest(ctx):
    await ctx.reply('it worked :triumph:')

@client.command('db_test')
async def db_test(ctx):
    await ctx.reply(await getdata())

@client.command('db_add_test')
async def db_add_test(ctx):
    await ctx.reply(await new_user(ctx.author))


# ECONOMY STUFF
@client.command('balance', help = 'Check user balance')
async def balance(ctx):
    await new_user(ctx.author)
    economy_dict = await getdata()
    
    bal_em = nextcord.Embed(title = f'Balance for {ctx.author.name}', color = random.choice(EMBED_COLORS))
    bal_em.add_field(name = 'Purse', value = economy_dict[str(ctx.author.id)]['purse'])
    bal_em.add_field(name = 'Bank', value = economy_dict[str(ctx.author.id)]['bank'])

    await ctx.reply(embed = bal_em)

async def new_user(user):
    '''
    economy_dict = await getdata()

    if str(user.id) in economy_dict:
        return False
    else:
        economy_dict[str(user.id)]['purse'] = 0
        economy_dict[str(user.id)]['bank'] = 0

    with open('mucho_dinero.json', 'w') as f:
        json.dump(economy_dict, f)
    '''
    test_data = await getdata()
    if str(user.id) in test_data:
        return False
    else:
        requests.post(f'{url}add={str(user.id)}')

async def getdata():
    '''
    with open('mucho_dinero.json', 'r') as f:
        return json.load(f)
    '''
    test_data = json.loads(requests.get(f'{url}get=all'))
    return test_data



client.run(os.environ['CLIENT_TOKEN'])