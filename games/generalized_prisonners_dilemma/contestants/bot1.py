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
        'Action.COOPERATE': {
            Action.COOPERATE: <int>
            Action.BETRAY: <int>
        }
        'Action.BETRAY': {
            Action.COOPERATE: <int>
            Action.BETRAY: <int>
        }
    }
}

PS! Acces potential payoff in the payoff matrix like this:
    game_log[my action][opponents action]
    E.g.: game_log[Action.BETRAY][Action.COOPERATE]
'''

class Contestant(ContestantTemplate):
    def action(self, game_log:dict) -> Action.__mro__[0]:
        return Action.COOPERATE
