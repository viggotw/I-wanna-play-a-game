from games.rock_paper_scissor.contestant_template import Action

class GameMechanics():
    MAX_PLAYERS = 2

    def __init__(self, players) -> None:
        self.players = players
        self.reset_players()

    def play(self):
        p0_action = self.players[0].action()
        p1_action = self.players[1].action()

        # Sanity-check on player actions
        assert p0_action in Action
        assert p1_action in Action
        
        # DRAW
        if p0_action == p1_action:
            p0_score = 0
            p1_score = 0

        # PLAYER 0 WINS
        elif (p0_action == Action.ROCK and p1_action == Action.SCISSOR) \
            or (p0_action == Action.PAPER and p1_action == Action.ROCK) \
            or (p0_action == Action.SCISSOR and p1_action == Action.PAPER):
            p0_score = 1
            p1_score = 0
        
        # PLAYER 1 WINS
        elif (p0_action == Action.ROCK and p1_action == Action.PAPER) \
            or (p0_action == Action.PAPER and p1_action == Action.SCISSOR) \
            or (p0_action == Action.SCISSOR and p1_action == Action.ROCK):
            p0_score = 0
            p1_score = 1

        self.players[0].update_scores_and_actions(p0_score, p0_action, p1_score, p1_action)
        self.players[1].update_scores_and_actions(p1_score, p1_action, p0_score, p0_action)

    def reset_players(self):
        for player in self.players:
            player.reset()

    def get_results(self):
        return [player.scores['self'] for player in self.players]
