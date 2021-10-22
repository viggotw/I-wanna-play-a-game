from games.game_log import GameLog

class GameEnvironmentGeneral():
    def __init__(self, max_players, turn_based):
        self.MAX_PLAYERS = max_players
        self.turn_based = turn_based  # Either turn-based or simultanous player execution
        self.new_game = None
        self.game_over = None
        self.game_log = None
        self.reset_game()

    def play(self, players):
        if self.new_game:
            self.new_game = False
            self.game_log = GameLog(players)

        if self.turn_based:
            for player in players:
                action = player.action(self.game_log.subjectify(player))
                score = self.get_reward(action)
                self.game_log.update_log(players, action, score)
        else:
            # If not turn-based, all players submit their action independently,
            # without any knowledge of the opponents actions
            actions = []
            for player in players:
                actions.append(player.action(self.game_log.subjectify(player)))
            scores = self.get_reward(actions)
            self.game_log.update_logs(players, actions, scores)

        

    def get_reward(self, action):
        raise NotImplemented()

    def reset_game(self, players=None):
        self.new_game = True
        self.game_over = False
        self.game_log = None
        if players:
            self._reset_players(players)

    def get_results(self):
        raise NotImplemented()

    def _reset_players(self, players):
        for player in players:
            player.reset()
