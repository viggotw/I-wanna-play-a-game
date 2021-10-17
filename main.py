from itertools import combinations

ITERATIONS_PER_TOURNAMENT = 100

# Load game
from games.rock_paper_scissor.game_machanics import GameMechanics

# Import all players
from games.rock_paper_scissor.contestants.player1 import Contestant as Player1
from games.rock_paper_scissor.contestants.player2 import Contestant as Player2
from games.rock_paper_scissor.contestants.player3 import Contestant as Player3


players = [Player1(), Player2(), Player3()]

# Create tournament
tournaments = combinations(players, GameMechanics.MAX_PLAYERS)

# Execute all tournaments
for contestants in tournaments:
    game = GameMechanics(contestants)
    for i in range(ITERATIONS_PER_TOURNAMENT):
        game.play()

    # Calculate scoreboard and appoint a winner
    print(contestants)
    print(game.get_results())