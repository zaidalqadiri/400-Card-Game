import random

class Card:
    def __init__(self, suit, rank):
        self.__suit = suit
        self.__rank = rank

    def __str__(self):
        return f"{self.__rank} of {self.__suit}"
    