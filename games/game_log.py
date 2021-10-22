from typing import Iterable


class GameLog():
    def __init__(self, players:list) -> None:
        self.players = players
        self.scores = None
        self.previous_moves = None
        self.init_log()

    def init_log(self):
        self.scores = {player: 0 for player in self.players}
        self.previous_moves = {player: [] for player in self.players}

    def update_move(self, player, new_move):
        self.previous_moves[player].append(new_move)

    def update_score(self, player, new_score):
        self.scores[player] += new_score

    def update_log(self, player, new_move, new_score):
        self.update_move(player, new_move)
        self.update_score(player, new_score)

    def update_logs(self, players, new_moves, new_scores):
        for player, new_move, new_score in zip(players, new_moves, new_scores):
            self.update_move(player, new_move)
            self.update_score(player, new_score)

    def clear_log(self):
        self.init_log()

    def get_scores(self, keys=None):
        if keys:
            if isinstance(keys, (list, tuple, set)):
                return [self.scores[key] for key in keys]
            else:
                return self.scores[keys]
        else:
            return self.scores

    def get_previous_moves(self, keys=None):
        if keys:
            if isinstance(keys, (list, tuple, set)):
                return [self.previous_moves[key] for key in keys]
            else:
                return self.previous_moves[keys]
        else:
            return self.previous_moves

    def subjectify(self, key):
        opponents = [player for player in self.players if player != key]
        return {
            'me': {
                'score': self.get_scores(key),
                'moves': self.get_previous_moves(key)
            },
            'opponents': {
                'score': self.get_scores(opponents),
                'moves': self.get_previous_moves(opponents)
            }
        }