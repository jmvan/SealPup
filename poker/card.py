

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


class Card:
    def __init__(self, value, suit) -> None:
        self.value = value
        self.suit = suit


class Deck:
    def __init__(self) -> None:
        cards = []
        for value in VALUES:
            for suit in SUITS:
                cards.append(Card(value, suit))
        self.cards = cards

    def draw(self) -> Card:
        return self.cards.pop()
