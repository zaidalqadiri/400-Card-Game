"""
This module defines the Game class which is responsible for the logic and rules of the card game.
The game consists of bidding phase, playing 13 rounds and scoring evalaution to see who the winner 
of the round is.
"""

from card import Deck
class Game:
    """
    Manages the logic and rules of the game

    Class Attributes:
        __current_round (int): Tracks the number of rounds played.
        __starting_index (int): Index of the player who starts each round.

    Instance Attributes:
        __players (list): A list of four Player objects.
        __teams (list): A list of two Team objects.
        __deck (Deck): The deck used in the current round.
        __trick_winner (Player): The player who won the last trick.
    """
    __current_round = 0
    __starting_index = 0

    def __init__(self, player1, player2, player3, player4, team1, team2):
        """
        Initializes the game with players and teams.

        Args:
            player1-4: Player instances representing each player.
            team1-2: Team instances for both teams.
        """
        self.__players = [player1, player2, player3, player4]
        self.__teams = [team1, team2]
        self.__deck = None
        self.__trick_winner = None

    def deal_cards(self):
        """
        Shuffles a new deck and deals 13 cards to each player.
        """
        self.__deck = Deck()
        for player in self.__players:
            cards = []
            for _ in range(13):
                cards.append(self.__deck.draw_card())
            player.set_hand(cards)
    
    def bid_phase(self):
        """
        Handles the bidding phase, including re-dealing if total bids are too low.
        """
        self.deal_cards()
        print("\nBidding Phase")
        print("--------------\n")

        for player in self.__players:
            print(player.show_hand())
            player.make_bid()
        print("\n--------------\n")

        if not self.valid_bids():
            print("***The sum of all players' bids is less than 11. Dealing cards again***")
            self.bid_phase()
    
    def valid_bids(self):
        """
        Checks if the sum of all players' bids is valid (>= 11).

        Returns:
            bool: True if total bid is valid, False otherwise.
        """
        total_bids = 0
        for player in self.__players:
            total_bids += player.get_bid()

        if total_bids < 11:
            return False
        
        return True

    def play_round(self):
        print(f"\n --- Round {self.__current_round + 1} ---\n")

        order = self.__players[self.__starting_index:] + self.__players[:self.__starting_index]
        cards_played = []

        # First player plays
        lead_card = order[0].play_card()
        lead_suit = lead_card.get_suit()
        cards_played.append((order[0], lead_card))
        print(f"{lead_card} played by {order[0].get_name()}\n\n\n")

         # Rest of the players
        for player in order[1:]:
            player_card = player.play_card(required_suit=lead_suit)
            cards_played.append((player, player_card))
            print(f"{player_card} played by {player.get_name()}\n\n\n")

        self.evaluate_tricks(lead_suit, cards_played)

        self.__current_round += 1
        self.__starting_index = self.__players.index(self.__trick_winner)  

    def evaluate_tricks(self, lead_suit, cards_played):
        # initialize the winning player and winning card to the player that plays thier card first and highest value to the first card played
        winning_player = cards_played[0][0]  
        winning_card = cards_played[0][1] 
        highest_value = cards_played[0][1].get_value()

        for player, card in cards_played[1:]:
            suit_played = card.get_suit()
            if ((suit_played == lead_suit and winning_card.get_suit() != "Heart" and card.get_value() > highest_value) or 
            (suit_played == "Heart" and winning_card.get_suit() != "Heart") or 
            (suit_played == "Heart" and winning_card.get_suit() == "Heart" and card.get_value() > highest_value)):
                winning_card = card
                winning_player = player
                highest_value = card.get_value()

        self.__trick_winner = winning_player  # track winner for the start of the next round

        winning_player.add_trick()
        print(f"{winning_card} wins the trick for {winning_player.get_name()}\n")
        
        for player in self.__players:
            print(f"{player.get_name()} has {player.get_tricks()} trick(s)")
        print("")
    
    def evaluate_game(self):
        for player in self.__players:
            player_bid = player.get_bid()
            player_tricks = player.get_tricks()
            if player_tricks >= player_bid:
                if player_bid >= 5:
                    player.increase_score(player_bid * 2)
                else:
                    player.increase_score(player_bid)
            else:
                player.decrease_score(player_bid)
            player.reset_tricks()
        
        self.__current_round = 0
        self.__starting_index = (self.__starting_index + 1) % 4  # rotate to next starter for next game
    
    def show_scores(self):
        print("\n\n\n")
        for player in self.__players:
            print(f"{player.get_name()}'s score: {player.get_score()}")
    
    def check_game_winner(self):
        for player in self.__players:
            if player.get_score() >= 41 and player.get_teammate().get_score() >= 0:
                print(f"\n\n{player.get_name()} and {player.get_teammate().get_name()} won!")
                return True 
        return False