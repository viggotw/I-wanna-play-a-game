import sys
from games.game_environment_general import GameEnvironmentGeneral
from games.generalized_prisonners_dilemma.contestant_template import Action
from games.generalized_prisonners_dilemma.config import ITERATIONS, NUM_PLAYERS, TURN_BASED, WIN_CRITERIA, PAYOFF_MATRICES

class GameEnvironment(GameEnvironmentGeneral):
    def __init__(self, suspense):
        super().__init__(ITERATIONS, NUM_PLAYERS, TURN_BASED, WIN_CRITERIA, suspense)

    def get_reward(self, moves:dict, game_board=None):
        
        ''' Calculate the score of each player
        :param moves: A dictionary with keys that equal the player name and a value
                      that is one of the possible Actions.
                      E.g: {'player1_name': Action1, 'player2_name': Action2}
        :param game_board: A dictionary with the payoff matrix, subjective for each player
        '''
        players = list(moves.keys())
        actions = [moves[player] for player in players]

        # Sanity-check on player actions
        assert actions[0] in Action
        assert actions[1] in Action
        
        # GET SCORES
        if actions[0] == Action.COOPERATE and actions[1] == Action.COOPERATE:
            print("O", end='')
            winner = None
        elif actions[0] == Action.COOPERATE and actions[1] == Action.BETRAY:
            print("<", end='')
            winner = players[1]
        elif actions[0] == Action.BETRAY and actions[1] == Action.COOPERATE:
            print(">", end='')
            winner = players[0]
        elif actions[0] == Action.BETRAY and actions[1] == Action.BETRAY:
            print("X", end='')
            winner = None
        else:
            raise ValueError(f"Unknown player action. {players[0]} played {actions[0]} and {players[1]} played {actions[1]}")

        rewards = game_board[players[0]][actions[0], actions[1]]


        self.game_over = True
        sys.stdout.flush()  # Forces the buffer to be written to stdout

        return {
            'winner': winner,
            'players': {
                players[0]: {
                    'action': actions[0],
                    'reward': rewards[0]
                },
                players[1]: {
                    'action': actions[1],
                    'reward': rewards[1]
                }
            }
        }

    def get_game_board(self, players, iteration:int):
        i = iteration
        return {
            players[0]: {
                (Action.COOPERATE, Action.COOPERATE): PAYOFF_MATRICES[i][0][0],
                (Action.COOPERATE,    Action.BETRAY): PAYOFF_MATRICES[i][0][1],
                (Action.BETRAY,    Action.COOPERATE): PAYOFF_MATRICES[i][1][0],
                (Action.BETRAY,       Action.BETRAY): PAYOFF_MATRICES[i][1][1]
            },
            players[1]: {
                (Action.COOPERATE, Action.COOPERATE): PAYOFF_MATRICES[i][0][0],
                (Action.COOPERATE,    Action.BETRAY): PAYOFF_MATRICES[i][1][0],
                (Action.BETRAY,    Action.COOPERATE): PAYOFF_MATRICES[i][0][1],
                (Action.BETRAY,       Action.BETRAY): PAYOFF_MATRICES[i][1][1]
            },
        }