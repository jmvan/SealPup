import discord
from enum import Enum

from typing import List
from player import Player


class GameState(Enum):
    WAIT_FOR_PLAYERS = 2
    DEALING = 3
    BETTING_PRE_FLOP = 4
    BETTING_FLOP = 5
    BETTING_TURN = 6
    BETTING_RIVER = 7
    SHOWDOWN = 8


class Game:
    def __init__(self) -> None:
        self.small_blind = 0.1
        self.big_blind = 0.2
        self.players: List[Player] = []
        self.betters: List[Player] = []
        self.board: List[Card] = []
        self.num_betters = 0
        self.round = 0
        self.pool = 0
        self.deck = None
        self.game_state = GameState.NO_GAME

    def add_player(self, user: discord.User):
        for player in self.players:
            if player.user == user:
                return False
        self.players.append(Player(user))
        return True

    def deal_hole_cards(self):

        for player in self.players:
            self.betters.append(player)

    def check_current_player(self, user: discord.User):
        current_player = self.betters.pop(0)
        if user == current_player:
            return True
        return False


