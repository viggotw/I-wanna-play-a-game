from games.game_environment_general import GameEnvironmentGeneral
from games.rock_paper_scissor.contestant_custom import Action
from games.rock_paper_scissor.config import MAX_PLAYERS, TURN_BASED

class GameEnvironment(GameEnvironmentGeneral):
    def __init__(self):
        super().__init__(MAX_PLAYERS, TURN_BASED)

    def get_reward(self, actions):
        p1_action = actions[0]
        p2_action = actions[1]

        # Sanity-check on player actions
        assert p1_action in Action
        assert p2_action in Action
        
        # DRAW
        if p1_action == p2_action:
            p1_score = 0
            p2_score = 0

        # PLAYER 0 WINS
        elif (p1_action == Action.ROCK and p2_action == Action.SCISSOR) \
            or (p1_action == Action.PAPER and p2_action == Action.ROCK) \
            or (p1_action == Action.SCISSOR and p2_action == Action.PAPER):
            p1_score = 1
            p2_score = 0
        
        # PLAYER 1 WINS
        elif (p1_action == Action.ROCK and p2_action == Action.PAPER) \
            or (p1_action == Action.PAPER and p2_action == Action.SCISSOR) \
            or (p1_action == Action.SCISSOR and p2_action == Action.ROCK):
            p1_score = 0
            p2_score = 1

        self.game_over = True

        return [p1_score, p2_score]

    def reset_players(self):
        for player in self.players:
            player.reset()

    def get_results(self):
        return [player.scores['self'] for player in self.players]
