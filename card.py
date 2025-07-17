'''
This module provides classes to represent a standard deck of playing cards.
It includes Card and Deck classes with functionality to initialize, shuffle,
and draw cards.
'''

import random

class Card:
    """
    Represents a playing card with a suit and a rank.
    
    Attributes:
        __suit (str): The suit of the card ('Diamond', 'Heart', 'Spade', 'Club').
        __rank (Union[int, str]): The rank of the card (2–10, 'J', 'Q', 'K', 'A').
    """

    def __init__(self, suit, rank):
        """
        Initializes a Card with a given suit and rank.

        Args:
            suit (str): The suit of the card.
            rank (int | str): The rank of the card.
        """
        self.__suit = suit
        self.__rank = rank

    def get_suit(self):
        """
        Initializes a Card with a given suit and rank.

        Args:
            suit (str): The suit of the card.
            rank (int or str): The rank of the card.
        """
        return self.__suit
    
    def get_value(self):
        """
        Returns the numeric value of the card's rank for comparison purposes.

        Returns:
            int: The numerical value of the card.
        """
        rank_order = {
            '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
            '7': 7, '8': 8, '9': 9, '10': 10,
            'J': 11, 'Q': 12, 'K': 13, 'A': 14
        }
        return rank_order[str(self.__rank)]

    def __str__(self):
        """
        Returns a string representation of the card.

        Returns:
            str: A string in the format "Rank of Suit".
        """
        return f"{self.__rank} of {self.__suit}"
    
class Deck:
    def __init__(self):
        suits = ['Diamond', 'Heart', 'Spade', 'Club']
        ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

        self.__deck = []

        for suit in suits:
            for rank in ranks:
                self.__deck.append(Card(suit, rank))

        random.shuffle(self.__deck)

    def shuffle(self):
        random.shuffle(self.__deck)
    
    def draw_card(self):
        return self.__deck.pop()