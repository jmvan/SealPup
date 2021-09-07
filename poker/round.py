import discord
from enum import Enum

from typing import List
from player import Player

class RoundState(Enum):
    NO_GAME = 1
    WAIT_FOR_PLAYERS = 2
    DEALING = 3
    BETTING_PREFLOP = 4
    BETTING_FLOP = 5
    BETTING_TURN = 6
    BETTING_RIVER = 7


class Round:
    def __init__(self) -> None:
        self.small_blind = 0.1
        self.big_blind = 0.2
        self.betters: List[Player] = []
        self.num_betters = 0
        self.round = 0
        self.pool = 0
        self.deck = None
        self.round_state = RoundState.NO_GAME

    def add_player(self, user: discord.User):
        for player in self.players:
            if player.user == user:
                return False
        self.players.append(Player(user))
        return True

    def deal_hole_cards(self):
        for player in self.players:
            self.betters.append(player)
        # deal the cards to the players










