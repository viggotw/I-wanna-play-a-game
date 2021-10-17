from enum import Enum
import os

class Action(Enum):
    ROCK = 'rock'
    PAPER = 'paper'
    SCISSOR = 'scissor'

class ContestantTemplate:
    def __init__(self) -> None:
        self.reset()

    def action(self) -> Action.__mro__[0]:
        raise NotImplemented('This line should be deleted and replaced by your custom code')

    def update_scores_and_actions(self, self_score, self_action, opponent_score, opponent_action) -> None:
        self.scores['self'] += self_score
        self.scores['opponent'] += opponent_score
        self.previous_actions['self'].append(self_action)
        self.previous_actions['opponent'].append(opponent_action)

    def reset(self):
        self.scores = {
            'self': 0,
            'opponent': 0
        }
        self.previous_actions = {
            'self': [],
            'opponent': []
        }