"""
This module defines the Player class used in a card game.
Each player has a name, a hand of cards, a bid, a score, and a teammate.
"""

class Player:
    """
    Represents a player in the card game.

    Attributes:
        __name (str): The name of the player.
        __cards (list): The cards currently held by the player.
        __bid (int): The bid made by the player.
        __score (int): The player's total score.
        __tricks (int): The number of tricks won by the player.
        __teammate (Player): The teammate of this player.
    """
    def __init__(self, name):
        """
        Initializes a Player with a name and default values.
        """
        self.__name = name
        self.__cards = []
        self.__bid = None
        self.__score = 0
        self.__tricks = 0
        self.__teammate = None

    def set_hand(self, cards):
        """
        Sets the player's hand.

        Args:
            cards (list): A list of Card objects.
        """
        self.__cards = cards
    
    def show_hand(self):
        """
        Returns a string representation of the player's hand.

        Returns:
            str: Formatted string showing all cards in hand.
        """
        return f"{self.get_name()}'s hand: {[str(card) for card in self.__cards]}\n"

    def set_teammate(self, player):
        """
        Sets the teammate for the player.

        Args:
            player (Player): The teammate to be set.
        """
        self.__teammate = player
        player.__teammate = self
    
    def get_teammate(self):
        """
        Returns the teammate of the player.

        Returns:
            Player: The teammate player object.
        """
        return self.__teammate
    
    def make_bid(self):
        """
        Prompts the user to input a bid value and sets it,
        with validation based on current score.
        """
        while True:
            try:
                user_input = int(input(f"input {self.__name}'s bid: "))
                print("\n\n\n")
            except ValueError:
                print("Invalid input. Please enter a whole number.\n")
                continue

            if user_input < 2 or user_input > 13:
                print("Your bid must be between 2 and 13\n")
                continue
            elif user_input == 2 and self.__score >= 30:
                print("The minimum bid for a score of 30 and above is 3\n")
                continue
            elif user_input == 3 and self.__score >= 40:
                print("The minimum bid for a score of 40 and above is 4\n")
                continue
            else:
                self.__bid = user_input
                break
    
    def get_bid(self):
        """
        Returns the bid made by the player.

        Returns:
            int: The bid value.
        """
        return self.__bid

    def increase_score(self, amount):
        self.__score += amount
    
    def decrease_score(self, amount):
        self.__score -= amount
    
    def play_card(self, required_suit = None):
        while True:
            print(self.show_hand())
            user_input = str(input(f"{self.get_name()}'s turn. Play a card (e.g. 3 of Spade): "))

            for card in self.__cards:
                if str(card).lower() == user_input.lower():
                    if required_suit and card.get_suit() != required_suit and self.has_suit(required_suit):
                        print(f"\nYou must play a {required_suit} if you have one.\n")
                        return self.play_card(required_suit)  # retry
                    self.__cards.remove(card)
                    return card

    def get_name(self):
        return self.__name

    def add_trick(self):
        self.__tricks += 1

    def get_tricks(self):
        return self.__tricks
    
    def has_suit(self, suit):
        return any(card.get_suit() == suit for card in self.__cards)
    
    def get_score(self):
        return self.__score
    
    def reset_tricks(self):
        self.__tricks = 0