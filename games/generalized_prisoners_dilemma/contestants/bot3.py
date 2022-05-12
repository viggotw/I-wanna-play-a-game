from games.generalized_prisoners_dilemma.contestant_template import ContestantTemplate, Action

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
    'game_board': {
        (Action.COOPERATE, Action.COOPERATE): (<int>,<int>)
        (Action.BETRAY,    Action.COOPERATE): (<int>,<int>)
        (Action.COOPERATE,    Action.BETRAY): (<int>,<int>)
        (Action.BETRAY,       Action.BETRAY): (<int>,<int>)
        }
    }
}

The payoff matrix can be thought of as follows
                                      opponent
             |          Cooperate         |            Betray          |
   ----------|----------------------------|----------------------------|
   Cooperate | <score:me>,<score:opponen> | <score:me>,<score:opponen> |
me ----------|----------------------------|----------------------------|
      Betray | <score:me>,<score:opponen> | <score:me>,<score:opponen> |
   ----------|----------------------------|----------------------------|

Acces potential payoff in the payoff matrix like this:
    game_log[my action, opponents action]
    E.g. game_log[Action.BETRAY, Action.COOPERATE]
'''

class Contestant(ContestantTemplate):
    def action(self, game_log:dict) -> Action:
        opponent_prev_moves = game_log['opponents']['moves'][0]
        if opponent_prev_moves:
            if opponent_prev_moves[-1] == Action.BETRAY:
                return Action.BETRAY
                
        return Action.COOPERATE
