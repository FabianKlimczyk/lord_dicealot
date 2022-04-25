import discord
import constants as cnst
import random

#create a connection to discord
client = discord.Client()

def isValidInput(input: str) -> bool:
    '''
    Checks if the given input is valid and is in the format [Number]+"W"+[Number]


    :param input: must contain W in between two numbers
    :return: True if input is valid
    '''
    noOfDice, seperator, diceValue = input.partition("W")
    return (noOfDice.isdecimal() and diceValue.isdecimal())


def rollNWM(input: str) -> str:
    '''
    rolls N M-sided dices

    :param input: consists of the nummber of dices N, the number M that represents the number of sides and the letter W
    :return: the dice result(s) as string
    '''
    if isValidInput(input):
        intValues = input.split("W")
        numberOfDices = int(intValues[0])
        nsided = int(intValues[1])
        output = ""
        for _ in range(numberOfDices):
            diceResult = random.randint(1,nsided)
            output += str(diceResult)+" "
        return output
    else:
        return f'{input} is not a valid input. Please write #help for additional information'


def help() -> str:
    #TODO "how to use the bot"
    return "help"


def errorMsg(msg: str) -> str:
    return f'{msg} is an invalid input. Please write #help for additional information'


@client.event
async def on_ready():
    # when the client has established a connection
    return f'{client.user} has connected to Discord!'


@client.event
async def on_message(message):
    # a message is send to the channel
    if message.author == client.user:
        return

    msg = message.content #text of the message

    if msg.startswith("#roll"): #prefix for commands
        printoutmsg = rollNWM(message.content[6:])
        await message.channel.send(printoutmsg)
    elif msg == "#help":
        helpmsg = help()
        await message.channel.send(helpmsg)
    elif msg.startswith("#"):
        errMsg = errorMsg(msg)
        await message.channel.send(errMsg)

client.run(cnst.TOKEN)