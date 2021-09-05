import discord

from typing import List
from player import Player


class Game():
    def __init__(self) -> None:
        self.small_blind = 0.1
        self.big_blind = 0.2
        self.players: List[Player] = []
        self.betters = []
        self.round = 0
        self.pool = 0
        self.deck = None

    def add_player(self, user: discord.User):
        for player in self.players:
            if player.user == user:
                return False
        self.players.append(Player(user))
        return True

    def deal_hands():








