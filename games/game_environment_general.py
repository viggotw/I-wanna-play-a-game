from typing import Union, List
from games.game_log import GameLog
from time import sleep

class GameEnvironmentGeneral():
    def __init__(self, iterations, max_players, turn_based, win_criteria, suspense):
        assert win_criteria in [
            'wins',  # Each round ends with a winner. The final winner is the player with the most wins
            'score'  # Each round ends with a score. The final winner is the player with the highest total score
        ]
        self.ITERATIONS = iterations
        self.MAX_PLAYERS = max_players
        self.TURN_BASED = turn_based  # Either turn-based or simultanous player execution
        self.WIN_CRITERIA = win_criteria
        self.suspense = suspense
        self.game_over = False
        self.shared_game_log = None

    def play(self, players, extra_info:Union[List[dict], dict, None]=None):
        ''' Executes a game played between 'players'. One game may consist of several rounds'''
        self.shared_game_log = GameLog(players)
        stats = {}
        for player in players:
            stats[player] = {
                'actions': [],
                'score': 0,
                'wins': 0
            }
            
        for i in range(self.ITERATIONS):  # A game may consist of multiple rounds or iterations
            data=None
            if extra_info:
                if isinstance(extra_info, dict):
                    data = extra_info
                elif isinstance(extra_info, list):
                    data = extra_info[i]

            while not self.game_over:  # A game is always played until the game_over stop criterion is set to True
                # Players do their action
                if self.TURN_BASED:  # Turn-based games enables the players to view the log of previous players from that round
                    for player in players:
                        action = player.action(self.shared_game_log.subjectify(player, data))
                        self.shared_game_log.update_move(player, action)
                else:  # If not turn-based, all players submit their action without any knowledge of the opponents actions
                    actions = []
                    for player in players:
                        action = player.action(self.shared_game_log.subjectify(player, data))
                        actions.append(action)
                    self.shared_game_log.update_moves(players, actions)

                # Based on player actions, calculate reward
                result = self.get_reward(self.shared_game_log.get_last_move(), data)
                
                # Upodate game log
                scores = [result['players'][player]['reward'] for player in players]
                self.shared_game_log.update_scores(list(players), scores)

            self.restart_game()
            if self.suspense: sleep(0.2)

        print()

        
        winners = []
        best_score = 0

        for player in players:
            stats[player]['actions'] = self.shared_game_log.get_previous_moves(player)
            stats[player]['score'] = self.shared_game_log.get_scores(player)
        
            if stats[player]['score'] > best_score:
                winners = [player]
                best_score = stats[player]['score']
            elif stats[player]['score'] == best_score:
                winners.append(player)
                
        for player in winners:
            stats[player]['wins'] = 1

        return stats
                

    def get_reward(self, moves:dict, data=None) -> dict:
        """ Game logic
        This should be implemented in each game environment in a class GameEnvironment(GameEnvironmentGeneral)"
        This is where you omplement the game logic, deciding which player is the winner and what reward they get.
        
        :param moves: A dictionary with keys that equal the player name and a value
                      that is one of the possible Actions.
                      E.g: {'player1_name': Action1, 'player2_name': Action2}
        :return dict:

        The return format looks like this:
        {
            'winner': <key in the 'moves' input dict>,
            'players': {
                'players1': {
                    'action': <defined in your contestant_template:Action>,
                    'reward': <int of float>
                },
                ...
            }
        }
        """
        raise NotImplemented()

    def restart_game(self):
        self.game_over = False

