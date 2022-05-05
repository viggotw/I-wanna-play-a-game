from games.rock_paper_scissor.contestant_template import Action, ContestantTemplate
""" GAME_LOG STRUCTURE
{
    'me': {
        'score': 0,
        'moves': []
    },
    'opponents': {
        'score': [0],
        'moves': [[]]
    }
}
"""
class Contestant(ContestantTemplate):
    counter = 0
    def action(self, game_log: dict) -> Action.__mro__[0]:
        prev_opponent_move = game_log["opponents"]["moves"][0]
        my_prev_move = game_log["me"]["moves"]
        if prev_opponent_move and len(my_prev_move) > 2:
            prev_opponent_move = prev_opponent_move[-1]
            my_prev_prev_move = my_prev_move[-2]
            if prev_opponent_move == my_prev_prev_move:
                self.counter += 1
            else:
                self.counter = 0
            if self.counter >= 2:
                return self.choose_beat_prev_ours(game_log)
            else:
                return self.choose_beats_last_opponent(game_log)
        else:
            return Action.ROCK
    def choose_beats_last_opponent(self, game_log: dict) -> Action.__mro__[0]:
        prev_opponent_move = game_log["opponents"]["moves"][0]
        if prev_opponent_move:
            if prev_opponent_move == Action.PAPER:
                return Action.SCISSOR
            elif prev_opponent_move == Action.SCISSOR:
                return Action.ROCK
            elif prev_opponent_move == Action.ROCK:
                return Action.PAPER
        return Action.PAPER
    def choose_beat_prev_ours(self, game_log: dict) -> Action.__mro__[0]:
        prev_opponent_move = game_log["opponents"]["moves"][0]
        if prev_opponent_move:
            if prev_opponent_move == Action.PAPER:
                return Action.ROCK
            elif prev_opponent_move == Action.SCISSOR:
                return Action.PAPER
            elif prev_opponent_move == Action.ROCK:
                return Action.SCISSOR
        return Action.PAPER
    def choose_same_as_opponent(self, game_log: dict) -> Action.__mro__[0]:
        prev_opponent_move = game_log["opponents"]["moves"][0]
        if prev_opponent_move:
            if prev_opponent_move == Action.PAPER:
                return Action.PAPER
            elif prev_opponent_move == Action.SCISSOR:
                return Action.SCISSOR
            elif prev_opponent_move == Action.ROCK:
                return Action.ROCK
        return Action.PAPER