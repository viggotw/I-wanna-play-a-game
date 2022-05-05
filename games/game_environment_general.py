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

    def play(self, players):
        ''' Executes a game played between 'players'. One game may consist of several rounds'''
        self.shared_game_log = GameLog(players)
        stats = {}
        for player in players:
            stats[player] = {
                'actions': [],
                'score': 0,
                'wins': 0
            }
            
        for _ in range(self.ITERATIONS):  # A game may consist of multiple rounds or iterations
            while not self.game_over:  # A game is always played until the game_over stop criterion is set to True
                if self.TURN_BASED:  # Turn-based games enables the players to view the log of previous players from that round
                    for player in players:
                        action = player.action(self.shared_game_log.subjectify(player))
                        self.shared_game_log.update_move(player, action)

                else:  # If not turn-based, all players submit their action without any knowledge of the opponents actions
                    actions = []
                    for player in players:
                        action = player.action(self.shared_game_log.subjectify(player))
                        actions.append(action)
                    self.shared_game_log.update_moves(players, actions)

                result = self.get_reward(self.shared_game_log.get_last_move())
                
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
                

    # def get_reward(self, action):
    #     raise NotImplemented()

    def restart_game(self):
        self.game_over = False

    def get_results(self):
        raise NotImplemented()
