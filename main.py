import discord
import os
from dotenv import load_dotenv
from typing import Dict, List

client = discord.Client()

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

    if message.content.startswith("!"):

        command_str = parse_game_command()

        # await message.channel.send("The Poker game is starting, type `!join` to enter the game.")

def parse_game_command(commands):



load_dotenv()
client.run(os.getenv('TOKEN'))
