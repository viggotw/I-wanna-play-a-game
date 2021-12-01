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
        for match_id, players in enumerate(matches):
            print(f"*** Match {match_id+1} (out of {len(matches)}):  {' vs. '.join(player.name for player in players)} ***")
            # Execute one game
            stats_current = game.play(players)

            # Update global score board
            for player in players:
                for key in self.stats_global[player]:
                    self.stats_global[player][key] += stats_current[player][key]
                sleep(1)
                print(f"{player}: {stats_current[player]['wins']} wins")
            print()
            sleep(1)

        self._print_scores()
        

    def _print_scores(self):
        scores = {str(player): stats['wins'] for player, stats in self.stats_global.items()}

        input("Tournament ended. Press a ENTER to get results...\n\n")
        print('*** FINAL SCORES ***')
        print("Placement       Name            Score")
        scores_sorted = dict(sorted(scores.items(), key=lambda item: item[1], reverse=False))
        for inv_placement, (player, score) in enumerate(scores_sorted.items()):
            placement = len(scores_sorted) - inv_placement
            sleep(2)
            print(f"{placement:>9}\t{player:<15}\t{score:>5}")
            

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
