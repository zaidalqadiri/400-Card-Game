# 🃏400 Card Game

A terminal-based simulation of the 400 card game, built with Python using Object-Oriented Programming principles.

## About the Game

400 is a strategic trick-taking card game usually played by four players in two teams. The game emphasizes teamwork, bidding, and carefully choosing when to play or hold back your strongest cards. This Python version replicates the core gameplay in the terminal.

## Features

- ♠️Full 52-card deck with realistic shuffling
- 🎯 Bidding system with dynamic rules based on score
- 💡Enforces players to follow the suit
- 🏆 Trick evaluation and scoring
- 🔄 Automatic redeal if total bids < 11
- 🔁 Rotating turn order: first player changes each round

## Code Structure

- Card: Represents a single card with rank and suit
- Deck: Handles card creation, shuffling, and dealing
- Player: Stores player info, hand, bids, and tricks won
- Team: Groups two players and assigns a team ID
- Game: Manages rounds, bidding, trick logic, and score evaluation

## How to Run

Make sure you have Python 3 installed.

```
git clone https://github.com/yourusername/400-card-game.git
cd 400-card-game
python3 400.py
```
You’ll be prompted to enter bids and play cards in the terminal.
