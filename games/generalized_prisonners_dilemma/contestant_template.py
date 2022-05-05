from games.contestant_general import ContestantGeneral
from enum import IntEnum

class Action(IntEnum):
    COOPERATE = 0
    BETRAY = 1

class ContestantTemplate(ContestantGeneral):
    def reset(self):
        pass  # TODO: Extend this