import discord
import os
from dotenv import load_dotenv

client = discord.Client()
game = None


@client.event
async def on_ready():
    print("{0} reporting for duty!".format(client.user))


@client.event
async def on_message(message):
    #  Do not allow the bot to reply to itself
    if message.author.id == client.user.id:
        return

    # Ignore empty messages
    if len(message.content.split()) == 0:
        return

    # Poker
    if message.content.startswith("!"):
        first_command = message.content.split()[0]
        process_poker_command()
        await message.channel.send("The Poker game is starting, type `!join` to enter the game." + first_command)


load_dotenv()
client.run(os.getenv('TOKEN'))
