import discord
from test import dicebot
from test import dicemax

client = discord.Client()
token = "NjQ5Njg5MTM1MTc4ODQyMTUx.XeBg5w.dNdVOWvx_ikM92gHxhNBGfM-Ag0"


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
    if message.content.startswith("/") and "k" not in message.content:
        newMessage = message.content.split("/")
        diceMessage = dicebot(newMessage[-1])
        await message.channel.send(diceMessage)
    if "/" and "d" and "k" in message.content and message.content.startswith("/"):
        newMessage = message.content.split("/")
        diceMessage = dicemax(newMessage[-1])
        await message.channel.send(diceMessage)


client.run(token)
