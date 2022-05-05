import sys
from games.game_environment_general import GameEnvironmentGeneral
from games.generalized_prisonners_dilemma.contestant_template import Action
from games.generalized_prisonners_dilemma.config import ITERATIONS, NUM_PLAYERS, TURN_BASED, WIN_CRITERIA

class GameEnvironment(GameEnvironmentGeneral):
    def __init__(self, suspense):
        super().__init__(ITERATIONS, NUM_PLAYERS, TURN_BASED, WIN_CRITERIA, suspense)

    def play(self, players):
        payoff_matrices = self._create_payoff_matrix(players)
        return super().play(players, extra_info=payoff_matrices)

    def get_reward(self, moves:dict, data):
        
        ''' Calculate the score of each player
        :param moves: A dictionary with keys that equal the player name and a value
                      that is one of the possible Actions.
                      E.g: {'player1_name': Action1, 'player2_name': Action2}
        '''
        players = list(moves.keys())
        actions = [moves[player] for player in players]

        # Sanity-check on player actions
        assert actions[0] in Action
        assert actions[1] in Action
        
        # GET SCORES
        # {
        #     players[0]: {'payoff_matrix': [[0, 2],[1,0]]},
        #     players[1]: {'payoff_matrix': [[1, 0],[0,2]]},
        # }

        # PRINT RESULT SYMBOL
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

        payoff_matrix = data[players[0]][0]['data']
        rewards = payoff_matrix[actions[0]][actions[1]]

        # rewards = [data[player][0]['data'][action] for player, action in zip(players, actions)]

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

    def _create_payoff_matrix(self, players):
        # TODO: Generate a list of length ITERATIONS with these dictionaries
        """
         (0,0)  |  (-1,-5)
        (-1,-5) | (-10,-10)
        """
        return {
            players[0]: [{'name': 'payoff_matrix', 'data': [[(-1,-1), (-3,0)],[(0,-3), (-2,-2)]]}],
            players[1]: [{'name': 'payoff_matrix', 'data': [[(-1,-1), (0,-3)],[(-3,0), (-2,-2)]]}],
        }