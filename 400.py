import random

class Card:
    def __init__(self, suit, rank):
        self.__suit = suit
        self.__rank = rank

    def __str__(self):
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

class Player:
    def __init__(self, name):
        self.__name = name
        self.__cards = []
        self.__bid = None
        self.__score = 0
        self.__tricks = 0
        self.__team = None

    def set_hand(self, cards):
        self.__cards = cards
    
    def show_hand(self):
        return f"{self.get_name()}'s hand: {[str(card) for card in self.__cards]}\n"
    
    def make_bid(self):
        while True:
            user_input = input(f"input {self.__name}'s bid: ")

            if user_input < '2' or user_input > 13:
                print("The minimum bid is 2 and the maximum bid 13")
                continue
            elif user_input == '2' and self.__score >= 30:
                print("The minimum bid for a score of 30 and above is 3")
                continue
            elif user_input == '3' and self.__score >= 40:
                print("The minimum bid for a score of 40 and above is 4")
                continue
            else:
                self.__bid = int(user_input)
                break
    
    def play_card(self, card):
        pass

    def get_name(self):
        return self.__name

class Team:
    _team_count = 0

    def __init__(self, player1, player2):
        self.__players = [player1, player2]
        Team._team_count += 1
        self.__team_id = Team._team_count
    
    def get_team_info(self):
        return f"Team {self.__team_id}: {self.__players[0].get_name()} and {self.__players[1].get_name()}"

class Game:

    _current_round = 0

    def __init__(self, player1, player2, player3, player4, team1, team2):
        self.__players = [player1, player2, player3, player4]
        self.__teams = [team1, team2]
        self.__deck = Deck()

    def start_game(self):
        for player in self.__players:
            cards = []
            for i in range(13):
                cards.append(self.__deck.draw_card())
            player.set_hand(cards)
    
    def bid_phase(self):
        print("\nBidding Phase")
        print("--------------\n")

        for player in self.__players:
            print(player.show_hand())
            player.make_bid()
        print("\n--------------\n")


    def play_round():
        pass

    def evaluate_tricks():
        pass 

p1 = Player("Zaid")
p2 = Player("Zai")
p3 = Player("Za")
p4 = Player("Z")

team1 = Team(p1, p2)
team2 = Team(p3, p4)

game = Game(p1, p2, p3, p4, team1, team2)
game.start_game()
game.bid_phase()