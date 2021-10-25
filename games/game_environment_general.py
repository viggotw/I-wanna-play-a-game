from games.game_log import GameLog

class GameEnvironmentGeneral():
    def __init__(self, iterations, max_players, turn_based):
        self.ITERATIONS = iterations
        self.MAX_PLAYERS = max_players
        self.TURN_BASED = turn_based  # Either turn-based or simultanous player execution
        self.game_over = False
        self.shared_game_log = None

    def play(self, players):
        self.shared_game_log = GameLog(players)
        stats = {
            player: {
                'num_matches': 0,
                'actions': [],
                'score': 0,
                'wins': 0,
                'draw': 0,
                'loss': 0,
            } for player in players
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
                
            # Update tournament stats
            for player in players:
                stats[player]['num_matches'] += 1
                if not result['winner']:
                    stats[player]['draw'] += 1
                elif result['winner'] == player:
                    stats[player]['wins'] += 1
                else:
                    stats[player]['loss'] += 1

            self.restart_game()


        for player in players:
            stats[player]['actions'] = self.shared_game_log.get_previous_moves(player)
            stats[player]['score'] = self.shared_game_log.get_scores(player)

        return stats
                

    # def get_reward(self, action):
    #     raise NotImplemented()

    def restart_game(self):
        self.game_over = False

    def get_results(self):
        raise NotImplemented()
