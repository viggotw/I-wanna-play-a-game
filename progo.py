import argparse
from tournament import Tournament

# Config
name = 'PROGO'
desc = "Welcome to PROGO, a game where players compete by submitting a bot that they script themselves"

epilog = 'Hope you enjoy playing! :)'
available_games = {
    'rock_paper_scissor': ['rock_paper_scissor', 'rps'],
    'generalized_prisoners_dilemma': ['generalized_prisoners_dilemma', 'gpd']
}
choices = [x for k in available_games for x in available_games[k]]

# PArse command line arguments
my_parser = argparse.ArgumentParser(prog=name, description=desc, epilog=epilog)

my_parser.add_argument('game',
                       type=str,
                       metavar='game',
                       help=f"Select game to play: {choices}",
                       choices=choices
                       )

my_parser.add_argument('-s', '--suspense',
                       type=bool,
                       default=False,
                       metavar='',
                       help="Set to `True` if you desire a more suspensfull tournament (default: `False`)",
                       required=False
                       )

args = my_parser.parse_args()


# Run game
for game_name, valid_names in available_games.items():
    if args.game in valid_names:
        tournament = Tournament(game_name, suspense=args.suspense)
        tournament.run()
        exit(0)
    
print("No game found with that name")
exit(1)