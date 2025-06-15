import random

class Card:
    def __init__(self, suit, rank):
        self.__suit = suit
        self.__rank = rank

    def get_suit(self):
        return self.__suit
    
    def get_value(self):
        rank_order = {
            '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
            '7': 7, '8': 8, '9': 9, '10': 10,
            'J': 11, 'Q': 12, 'K': 13, 'A': 14
        }
        return rank_order[str(self.__rank)]

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
            user_input = int(input(f"input {self.__name}'s bid: \n"))

            if user_input < 2 or user_input > 13:
                print("The minimum bid is 2 and the maximum bid 13")
                continue
            elif user_input == 2 and self.__score >= 30:
                print("The minimum bid for a score of 30 and above is 3")
                continue
            elif user_input == 3 and self.__score >= 40:
                print("The minimum bid for a score of 40 and above is 4")
                continue
            else:
                self.__bid = user_input
                break
    
    def get_bid(self):
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

class Team:
    _team_count = 0

    def __init__(self, player1, player2):
        self.__players = [player1, player2]
        Team._team_count += 1
        self.__team_id = Team._team_count
    
    def get_team_info(self):
        return f"Team {self.__team_id}: {self.__players[0].get_name()} and {self.__players[1].get_name()}"

class Game:

    __current_round = 0
    __starting_index = 0

    def __init__(self, player1, player2, player3, player4, team1, team2):
        self.__players = [player1, player2, player3, player4]
        self.__teams = [team1, team2]
        self.__deck = Deck()

    def deal_cards(self):
        for player in self.__players:
            cards = []
            for _ in range(13):
                cards.append(self.__deck.draw_card())
            player.set_hand(cards)
    
    def bid_phase(self):
        print("\nBidding Phase")
        print("--------------\n")

        for player in self.__players:
            print(player.show_hand())
            player.make_bid()
        print("\n--------------\n")
    
    def valid_bids(self):
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
        print(f"{lead_card} played by {order[0].get_name()}\n")

         # Rest of the players
        for player in order[1:]:
            player_card = player.play_card(required_suit=lead_suit)
            cards_played.append((player, player_card))
            print(f"{player_card} played by {player.get_name()}\n")

        self.__current_round += 1
        self.__starting_index = (self.__starting_index + 1) % 4  # Rotate starter for next round

        self.evaluate_tricks(lead_suit, cards_played)

    def evaluate_tricks(self, lead_suit, cards_played):
        winning_player = None
        winning_card = None
        highest_value = -1

        for player, card in cards_played:
            if card.get_suit() == lead_suit and card.get_value() > highest_value:
                winning_card = card
                winning_player = player
                highest_value = card.get_value()

        winning_player.add_trick()
        print(f"{winning_card} wins the trick for {winning_player.get_name()}\n")
        
        for player in self.__players:
            print(f"{player.get_name()} has {player.get_tricks()} trick(s)")
        print("")

        return winning_player
    
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

    
    def check_scores(self):
        for player in self.__players:
            print(f"{player.get_name()}'s score: {player.get_score()}")

p1 = Player("Dan")
p2 = Player("John")
p3 = Player("Eric")
p4 = Player("Alex")

team1 = Team(p1, p2)
team2 = Team(p3, p4)

game = Game(p1, p2, p3, p4, team1, team2)

while True:
    game.deal_cards()
    game.bid_phase()
    if not game.valid_bids():
        print("The sum of all players' bids is less than 11. Dealing cards again")
        continue
    else:
        break

for _ in range(13):
    game.play_round()
game.evaluate_game()
game.check_scores()
