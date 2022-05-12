from games.rock_paper_scissor.contestant_template import ContestantTemplate, Action
''' GAME_LOG STRUCTURE
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
'''
seed1 = [Action.SCISSOR, Action.ROCK, Action.SCISSOR, Action.ROCK, Action.ROCK]
seed2 = [Action.PAPER, Action.SCISSOR, Action.SCISSOR, Action.ROCK, Action.PAPER]
seed3 = [Action.SCISSOR, Action.PAPER, Action.ROCK, Action.SCISSOR, Action.ROCK]
moves = iter((seed1 + seed2 + seed3)*11999)
class Contestant(ContestantTemplate):
    def action(self, game_log:dict) -> Action:
        opponents_last_moves = []
        our_moves = game_log["me"]["moves"]
        if game_log['opponents']['moves'][0]:
            opponents_last_moves = game_log['opponents']['moves'][0]
        if len(opponents_last_moves) >= 10 and all([Action.ROCK == move for move in opponents_last_moves]):
            return Action.PAPER
        # elif len(opponents_last_moves) > 0:
        #     if our_moves[-1] == Action.PAPER:
        #         return Action.ROCK
        #     elif our_moves[-1] == Action.ROCK:
        #         return Action.SCISSOR
        #     else:
        #         return Action.PAPER
        # elif len(opponents_last_moves) == 0:
        #     return Action.PAPER  # todo
        move = next(moves)
        return move