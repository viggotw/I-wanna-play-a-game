from games.rock_paper_scissor.contestant_template import ContestantTemplate, Action
from random import choice

class Contestant(ContestantTemplate):
    def action(self) -> Action.__mro__[0]:
        if self.previous_actions['opponent'] == Action.ROCK:
            return Action.PAPER
        elif self.previous_actions['opponent'] == Action.PAPER:
            return Action.SCISSOR
        else: # initial move and if self.previous_actions['opponent'] == Action.SCISSOR:
            return Action.ROCK
