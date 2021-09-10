class Player:
    """
    A class representing a single poker player and its attributes
    """

    def __init__(self, discord_user) -> None:
        self.balance = 0
        self.user = discord_user
        self.first_card = None
        self.second_card = None
        self.bet_amount = 0
