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

def win_loss(action):
    pass

class Contestant(ContestantTemplate):
    def action(self, game_log:dict) -> Action:
        opponents_last_move = None
        if game_log['opponents']['moves'][0]:
            opponents_last_move = game_log['opponents']['moves'][0][-1]
            try:
                opponents_next_last_move = game_log['opponents']['moves'][0][-2]
            except IndexError:
                pass
        if game_log['me']['moves']:
            my_last_move = game_log['me']['moves'][-1]
        # won = last_round_won(my_last_move, opponents_last_move)
        
        

        if opponents_last_move is None:
            return Action.PAPER
        elif opponents_last_move == my_last_move:
            if my_last_move == Action.ROCK:
                return Action.PAPER
            elif my_last_move == Action.PAPER:
                return Action.SCISSOR
            else:
                return Action.ROCK
        elif (opponents_last_move == Action.PAPER and my_last_move == Action.SCISSOR) or (opponents_last_move == Action.SCISSOR and my_last_move == Action.ROCK) or (opponents_last_move == Action.ROCK and my_last_move == Action.PAPER):
            return opponents_last_move
        elif len(game_log['me']['moves'])>=2:
            two_last_moves = game_log['me']['moves'][-2:]
            if two_last_moves[0] == two_last_moves[1]:
                return opponents_last_move
            else:
                return my_last_move
        else:
            return Action.PAPER