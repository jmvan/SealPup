import os
import discord
from dotenv import load_dotenv
from poker.poker import Poker

client = discord.Client()
poker = Poker()


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
    if message.content.startswith("?"):
        poker.process_game_state(message=message)

load_dotenv()
client.run(os.getenv('TOKEN'))

