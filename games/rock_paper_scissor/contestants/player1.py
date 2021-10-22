from games.game_log import GameLog
from games.rock_paper_scissor.contestant_custom import ContestantCustom, Action

class Contestant(ContestantCustom):
    def action(self, game_log:dict) -> Action.__mro__[0]:
        return Action.ROCK
