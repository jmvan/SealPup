import discord
from enum import Enum

from deck import Deck
from card import Card
from typing import List
from player import Player


class GameState(Enum):
    WAIT_FOR_PLAYERS_PHASE = 1
    DEALING_PHASE = 2
    BETTING_PHASE = 3
    SHOWDOWN_PHASE = 4


class Game:
    def __init__(self) -> None:
        self.small_blind = 0.1
        self.big_blind = 0.2
        self.players: List[Player] = []
        self.betters: List[Player] = []
        self.board: List[Card] = []
        self.pool = 0
        self.deck: Deck = Deck()
        self.game_state: GameState = GameState.NO_GAME

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

    def deal_cards(self):

        # Deal cards for flop, river, turn
        self.board.append(self.deck.draw())
        self.board.append(self.deck.draw())
        self.board.append(self.deck.draw())
        self.board.append(self.deck.draw())
        self.board.append(self.deck.draw())

        # Deal two cards to each player
        self.betters = self.players.copy()
        for better in self.betters:
            better.first_card = self.deck.draw()
            better.second_card = self.deck.draw()

    def get_current_better(self):
        return self.betters[0]

    def verify_check(self, user: discord.User):
        if
        

    def verify_raise(self):

    def verify_


