import discord
import os
from dotenv import load_dotenv
from poker.game_state import GameState

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
    if message.content.startswith("!"):
        first_command = message.content.split()[0]
        game_state.process_command(message=message, command=first_command)
        await message.channel.send("The Poker game is looking for players\n" +
                                   "Type `!join` to join the game\n" +
                                   "Type '!deal` to start the game")


load_dotenv()
client.run(os.getenv('TOKEN'))
