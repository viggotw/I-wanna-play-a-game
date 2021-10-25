import pkgutil
import json
from importlib import import_module
from itertools import combinations
from time import sleep

class Tournament():
    def __init__(self, game_name, iter=100) -> None:
        self.game_env = self._load_game_environment_class(game_name)
        self.contestants = self._load_contestants(game_name)
        self.stats = {}

    def run(self):
        # Create all matches
        game = self.game_env.GameEnvironment()
        matches = list(combinations(self.contestants, game.MAX_PLAYERS))
        self.stats_global = {
            contestant: {
                'num_matches': 0,
                'score': 0,
                'wins': 0,
                'draw': 0,
                'loss': 0
            }
            for contestant in self.contestants
        }

        # Execute all matches
        for players in matches:
            print(f"*** {players} ***")
            stats_current = game.play(players)

            for player in players:
                for key in self.stats_global[player]:
                    self.stats_global[player][key] += stats_current[player][key]

                print(f"{player}: {stats_current[player]['wins']} wins")
            print()
            sleep(1)

        scores = {str(player): stats['wins'] for player, stats in self.stats_global.items()}
        print('FINAL SCORES')
        print(json.dumps(dict(sorted(scores.items(), key=lambda item: item[1], reverse=True)), indent=4))


        # Calculate scoreboard and appoint a winner
        #print(self.stats_global)




    def _load_game_environment_class(self, game_name):
        return import_module(f'games.{game_name}.game_environment')
    
    def _load_contestants(self, game_name):
        available_contestant_modules = pkgutil.iter_modules([f'./games/{game_name}/contestants'])
        contestant_paths = {
            module.name: f'games.{game_name}.contestants.{module.name}'
            for module in available_contestant_modules
            }
        return [import_module(contestant_path).Contestant(name)
            for name, contestant_path in contestant_paths.items()
        ]
