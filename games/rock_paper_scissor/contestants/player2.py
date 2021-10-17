from games.rock_paper_scissor.contestant_template import ContestantTemplate, Action
from random import choice

class Contestant(ContestantTemplate):
    def action(self) -> Action.__mro__[0]:
        return choice([Action.ROCK, Action.PAPER, Action.SCISSOR])
