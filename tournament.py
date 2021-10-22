import pkgutil
from importlib import import_module
from itertools import combinations
from typing import final

class Tournament():
    def __init__(self, game_name, iter=100) -> None:
        self.Game = self._load_game_environment_class(game_name)
        self.contestants = self._load_contestants(game_name)
        self.ITER = iter  # Iterations per game

    def run(self):
        # Create tournament
        game = self.Game()
        tournaments = list(combinations(self.contestants, game.MAX_PLAYERS))

        # Execute all tournaments
        for players in tournaments:
            for i in range(self.ITER):
                print(i)
                while not game.game_over:
                    game.play(players)
                game.reset_game()


            print(players)
            #for i in range(self.ITER):
            #    self.game.play()

        # Calculate scoreboard and appoint a winner
        print(self.contestants)
        #print(self.game.get_results())

    def _load_game_environment_class(self, game_name):
        return import_module(f'games.{game_name}.game_environment').GameEnvironment
    
    def _load_contestants(self, game_name):
        available_contestant_modules = pkgutil.iter_modules([f'./games/{game_name}/contestants'])
        contestant_paths = {
            module.name: f'games.{game_name}.contestants.{module.name}'
            for module in available_contestant_modules
            }
        return [import_module(contestant_path).Contestant(name)
            for name, contestant_path in contestant_paths.items()
        ]
