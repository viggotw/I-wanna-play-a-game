from games.rock_paper_scissor.contestant_template import ContestantTemplate, Action

class Contestant(ContestantTemplate):
    def action(self) -> Action.__mro__[0]:
        return Action.ROCK
