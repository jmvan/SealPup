import discord
from enum import Enum

from deck import Deck
from card import Card
from typing import List
from player import Player


class GameState(Enum):
    WAITING_PHASE = 1
    DEALING_PHASE = 2
    PRE_FLOP_PHASE = 3
    FLOP_PHASE = 4
    TURN_PHASE = 5
    RIVER_PHASE = 6
    SHOWDOWN_PHASE = 7


class Game:
    """
    This class contains the attributes and functions needed to run a poker game.
    """
    def __init__(self) -> None:
        self.small_blind = 0.1
        self.big_blind = 0.2
        self.players: List[Player] = []
        self.betters: List[Player] = []
        self.board: List[Card] = []
        self.pool = 0
        self.round = 0
        self.deck: Deck = Deck()
        self.game_state: GameState = GameState.WAITING_PHASE

    def reset_round(self):
        self.betters: List[Player] = []
        self.pool = 0
        self.board: List[Card] = []
        self.deck: Deck = Deck()

    def add_player(self, user: discord.User):
        for player in self.players:
            if player.user == user:
                return False
        self.players.append(Player(user))
        return True

    # Deal two cards to each player
    def deal_hole_cards(self):
        self.betters = self.players.copy()
        for better in self.betters:
            better.first_card = self.deck.draw()
            better.second_card = self.deck.draw()

    def get_current_better(self):
        return self.betters[0]

