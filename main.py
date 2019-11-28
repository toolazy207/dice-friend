import discord
from test import dicebot

client = discord.Client()


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("!"):
        newMessage = message.content.split("!")
        diceMessage = dicebot(newMessage[-1])
        await message.channel.send(diceMessage)

client.run("NjQ5Njg5MTM1MTc4ODQyMTUx.XeAcSw.1Bknlnw1VWoGVyjvXAC63mK-c84")
