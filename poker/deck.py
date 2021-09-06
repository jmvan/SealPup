import random
from card import Card

SUITS = ["S", "C", "D", "H"]

VALUES = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}


class Deck:
    def __init__(self) -> None:
        new_cards = []
        for value in VALUES:
            for suit in SUITS:
                new_cards.append(Card(value, suit))
        random.shuffle(new_cards)
        self.cards = new_cards

    def draw(self) -> Card:
        return self.cards.pop()


