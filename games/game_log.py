from typing import Iterable


class GameLog():
    def __init__(self, players:list) -> None:
        self.players = players
        self.scores = None
        self.previous_moves = None
        self.init_log()

    def init_log(self):
        ''' Initializes the log '''
        self.scores = {player: 0 for player in self.players}
        self.previous_moves = {player: [] for player in self.players}

    def update_move(self, player, new_move):
        ''' Adds a new move to a specific's player move log '''
        self.previous_moves[player].append(new_move)

    def update_moves(self, players, new_moves):
        ''' Update move logs for multiple players '''
        for player, new_move in zip(players, new_moves):
            self.update_move(player, new_move)

    def update_score(self, player, new_score):
        ''' Adds the new score to a specific's player score log '''
        self.scores[player] += new_score

    def update_scores(self, players, new_scores):
        ''' Update score logs for multiple players '''
        for player, new_score in zip(players, new_scores):
            self.update_score(player, new_score)

    def update_log(self, player, new_move, new_score):
        ''' Updates both the move and score logs of a specific player '''
        self.update_move(player, new_move)
        self.update_score(player, new_score)

    def update_logs(self, players, new_moves, new_scores):
        ''' Update move and score logs for multiple players '''
        for player, new_move, new_score in zip(players, new_moves, new_scores):
            self.update_move(player, new_move)
            self.update_score(player, new_score)

    def clear_log(self):
        ''' Clears all logs '''
        self.init_log()

    def get_scores(self, keys=None):
        ''' Get the scores for on or more players
        :param keys: If None, return all scores.
                     If list, return scores to players in list.
                     Else, return scores for specific player
        '''
        if keys:
            if isinstance(keys, list):
                return [self.scores[key] for key in keys]
            else:
                return self.scores[keys]
        else:
            return self.scores

    def get_last_move(self, keys=None):
        ''' Get only the last move from selected players
        :param keys: If None, return all previous moves.
                     If list, return previous moves to players in list.
                     Else, return previous moves for specific player
        '''
        if keys:
            if isinstance(keys, list):
                return [self.previous_moves[key][-1] for key in keys]
            else:
                return self.previous_moves[keys][-1]
        else:
            return {key: self.previous_moves[key][-1] for key in self.previous_moves.keys()}


    def get_previous_moves(self, keys=None):
        ''' Get the previous moves for on or more players
        :param keys: If None, return all previous moves.
                     If list, return previous moves to players in list.
                     Else, return previous moves for specific player
        '''
        if keys:
            if isinstance(keys, list):
                return [self.previous_moves[key] for key in keys]
            else:
                return self.previous_moves[keys]
        else:
            return self.previous_moves

    def subjectify(self, player, game_board:dict=None):
        ''' Transform the log into a subjective 'me vs. opponent' structure from the perspective of "key" that is easy for players to interact with
        :param player: key that exists in 'scores' and 'previous_moves'
        :param game_bord: the game board that should be passed to the players. 
                           This should be a dict containing all player keys
                           If this should be subjective to the player, this has to be done handled in advance
        Example input:
        game_board = 
        {
            players[0]: {(...)},
            players[1]: {(...)},
            (...)
        }
        '''

        opponents = [opponent for opponent in self.players if opponent != player]
        subjective_game_log = {
            'me': {
                'score': self.get_scores(player),
                'moves': self.get_previous_moves(player)
            },
            'opponents': {
                'score': self.get_scores(opponents),
                'moves': self.get_previous_moves(opponents)
            },
        }

        if game_board:
            subjective_game_log['game_board'] = game_board[player]

        return subjective_game_log