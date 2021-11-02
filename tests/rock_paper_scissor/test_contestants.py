import unittest
import pkgutil
from importlib import import_module
from games import rock_paper_scissor
from games.rock_paper_scissor.contestant_custom import Action

GAME_NAME = 'rock_paper_scissor'

input_generator = lambda score_self=0, moves_self=[], score_opponent=[0], moves_opponent=[[]]: {
    'me': {
        'score': score_self,
        'moves': moves_self
    },
    'opponents': {
        'score': score_opponent,
        'moves': moves_opponent
    }
}

class TestContestants(unittest.TestCase):
    def setUp(self) -> None:
        self.contestants = self.load_contestants(GAME_NAME)

    def load_contestants(self, game_name):
        available_contestant_modules = pkgutil.iter_modules([f'./games/{game_name}/contestants'])
        contestant_paths = {
            module.name: f'games.{game_name}.contestants.{module.name}'
            for module in available_contestant_modules
            }
        return [import_module(contestant_path).Contestant(name)
            for name, contestant_path in contestant_paths.items()
        ]

    def general_test(self, input):
        for contestant in self.contestants:
            try:
                action = contestant.action(input)
                assert action in Action
            except Exception as exception:
                raise AssertionError(f"EXCEPTION: {contestant}: {exception}")

    def test_read_contestans(self):
        print("\nCONTESTANTS:")
        for contestant in self.contestants:
            print(contestant.name)

    def test_first_action(self):
        self.general_test(input_generator())

    def test_previous_draw_rock(self):
        self.general_test(input_generator(0, [Action.ROCK], [0], [[Action.ROCK]]))

    def test_previous_draw_paper(self):
        self.general_test(input_generator(0, [Action.PAPER], [0], [[Action.PAPER]]))

    def test_previous_draw_scissor(self):
        self.general_test(input_generator(0, [Action.SCISSOR], [0], [[Action.SCISSOR]]))

    def test_previous_win_rock(self):
        self.general_test(input_generator(0, [Action.ROCK], [0], [[Action.SCISSOR]]))

    def test_previous_win_paper(self):
        self.general_test(input_generator(0, [Action.PAPER], [0], [[Action.ROCK]]))

    def test_previous_win_scissor(self):
        self.general_test(input_generator(0, [Action.SCISSOR], [0], [[Action.PAPER]]))

    def test_previous_loss_rock(self):
        self.general_test(input_generator(0, [Action.ROCK], [0], [[Action.PAPER]]))

    def test_previous_loss_paper(self):
        self.general_test(input_generator(0, [Action.PAPER], [0], [[Action.SCISSOR]]))

    def test_previous_loss_scissor(self):
        self.general_test(input_generator(0, [Action.SCISSOR], [0], [[Action.ROCK]]))
    


if __name__ == '__main__':
    unittest.main()