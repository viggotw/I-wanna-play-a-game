from games.game_log import GameLog
from games.rock_paper_scissor.contestant_custom import ContestantCustom, Action
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

class Contestant(ContestantCustom):
    def action(self, game_log:dict) -> Action.__mro__[0]:
        return choice([Action.ROCK, Action.PAPER, Action.SCISSOR])
