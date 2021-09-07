import discord
import os
from dotenv import load_dotenv
from poker.poker import GameState

client = discord.Client()
game_state = GameState()


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
        game_state.process_command(message=message)

load_dotenv()
client.run(os.getenv('TOKEN'))
