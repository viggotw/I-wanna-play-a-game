from games.rock_paper_scissor.contestant_template import ContestantTemplate, Action

''' GAME_LOG STRUCTURE
{
    'me': {
        'score': 0,
        'moves': []
    },
    'opponents': {
        'score': [0],
        'moves': [[]]
    }
}
'''


class Contestant(ContestantTemplate):
    last_score = 0
    losing_counter = 0

    def strat_1(self, game_log:dict) -> Action:
        opponents_last_move = None
        if game_log['opponents']['moves'][0]:
            opponents_last_move = game_log['opponents']['moves'][0][-1]

        if opponents_last_move == Action.ROCK:
            return Action.PAPER
        elif opponents_last_move == Action.PAPER:
            return Action.SCISSOR
        else: # initial move and if self.previous_actions['opponent'] == Action.SCISSOR:
            return Action.ROCK
        
    def strat_2(self, game_log:dict) -> Action.__mro__[0]:
        opponents_last_move = None
        if game_log['opponents']['moves'][0]:
            #if len(game_log['opponents']['moves'][0]) > 2:
            opponents_last_move = game_log['opponents']['moves'][0][-1]

        if opponents_last_move == Action.ROCK:
            return Action.SCISSOR
        elif opponents_last_move == Action.PAPER:
            return Action.ROCK
        else: # initial move and if self.previous_actions['opponent'] == Action.SCISSOR:
            return Action.PAPER

    def strat_3(self, game_log:dict) -> Action.__mro__[0]:
        opponents_last_move = None
        if game_log['opponents']['moves'][0]:
            #if len(game_log['opponents']['moves'][0]) > 3:
            opponents_last_move = game_log['opponents']['moves'][0][-1]

        if opponents_last_move == Action.ROCK:
            return Action.ROCK
        elif opponents_last_move == Action.PAPER:
            return Action.PAPER
        else: # initial move and if self.previous_actions['opponent'] == Action.SCISSOR:
            return Action.SCISSOR

    strategy = strat_1

    def change_strategy(self):
        if self.strategy == self.strat_1:
            self.strategy = self.strat_2
        elif self.strategy == self.strat_2:
            self.strategy = self.strat_3
        else:
            self.strategy = self.strat_1

    def action(self, game_log:dict) -> Action.__mro__[0]:
        winning = False
        if game_log["me"]["score"] > self.last_score:
            winning = True
            self.losing_counter = 0
        else:
            self.losing_counter += 1
        self.last_score = game_log["me"]["score"]
        
        if self.losing_counter % 2 == 0 and not winning:
            self.change_strategy()
            self.losing_counter = 0

        return self.strategy(game_log)