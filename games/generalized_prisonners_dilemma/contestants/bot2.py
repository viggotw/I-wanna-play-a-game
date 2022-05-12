from games.generalized_prisonners_dilemma.contestant_template import ContestantTemplate, Action

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
    'payoff_matrix': {
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
        pm = game_log['game_board']  # payoff matrix
        
        # Check if cooperating is always best
        if (pm[Action.COOPERATE, Action.COOPERATE] >= pm[Action.BETRAY, Action.COOPERATE]) and \
           (pm[Action.COOPERATE, Action.BETRAY] >= pm[Action.BETRAY, Action.BETRAY]):
           return Action.COOPERATE

        # Check if betraying is always best
        elif (pm[Action.BETRAY, Action.COOPERATE] >= pm[Action.COOPERATE, Action.COOPERATE]) and \
             (pm[Action.BETRAY, Action.BETRAY] >= pm[Action.COOPERATE, Action.BETRAY]):
            return Action.BETRAY

        else:
            return Action.COOPERATE