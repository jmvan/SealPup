class Card:
    """
    A class representing a single playing card.
    """
    def __init__(self, rank, suit) -> None:
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return self.rank + " " + self.suit
