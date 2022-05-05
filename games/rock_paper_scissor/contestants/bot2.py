from games.rock_paper_scissor.contestant_template import ContestantTemplate, Action
from random import choice

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

class Contestant(ContestantTemplate):
    def action(self, game_log:dict) -> Action.__mro__[0]:
        return choice([Action.ROCK, Action.PAPER, Action.SCISSOR])
