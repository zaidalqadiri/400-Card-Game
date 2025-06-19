from player import Player
from team import Team
from game import Game
from utils import assign_teams

def main():

    print("Welcome to the 400 card game!\n\n")

    player_names = [input(f"Input the name of player {i+1}: ") for i in range(4)]
    players = [Player(name) for name in player_names]

    print("\nSetting up teams...\n")

    p1, p2, p3, p4, team1, team2 = assign_teams(players)

    print(team1.get_team_info())
    print(team2.get_team_info())

    game = Game(p1, p2, p3, p4, team1, team2)

    while not game.check_game_winner():
        game.bid_phase()

        for _ in range(13):
            game.play_round()
        game.evaluate_game()
        game.show_scores()

if __name__ == "__main__":
    main()
