from games.game_log import GameLog

class ContestantGeneral():
    def __init__(self, name) -> None:
        self.name = name
        self.reset()

    def action(self, game_log:GameLog):
        raise NotImplemented('Use this method to implement your custom strategy')

    def reset(self):
        raise NotImplemented()

    def __repr__(self) -> str:
        return self.name