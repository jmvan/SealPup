import discord
from enum import Enum

from typing import List
from player import Player

class GameState(Enum):
    NO_GAME = 1
    WAIT_FOR_PLAYERS = 2
    PREFLOP = 3
    DEALING = 3
    PREFLOP = 4
    BETTING_FLOP = 5
    BETTING_TURN = 6
    BETTING_RIVER = 7


class Round():
    def __init__(self) -> None:
        self.small_blind = 0.1
        self.big_blind = 0.2
        self.players: List[Player] = []
        self.cur_betters = []
        self.num_betters = 0
        self.round = 0
        self.pool = 0
        self.deck = None
        self.game_state =

    def add_player(self, user: discord.User):
        for player in self.players:
            if player.user == user:
                return False
        self.players.append(Player(user))
        return True

    def deal_hands():








