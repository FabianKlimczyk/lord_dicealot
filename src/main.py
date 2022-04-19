import discord
import constants as cnst

#create a connection to discord
client = discord.Client()
#bot = commands.Bot(command_prefix='.', description=description)


@client.event
async def on_ready():
    # when the client has established a connection
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #TODO

client.run(cnst.TOKEN)