import argparse
from tournament import Tournament

# Config
name = 'PROGO'
desc = "Welcome to PROGO, a game where players compete by submitting a bot that they script themselves"
epilog = 'Hope you enjoy playing! :)'
available_games = {
    'rock_paper_scissor': ['rock_paper_scissor', 'rps'],
    'generalized_prisonners_dilemma': ['generalized_prisonners_dilemma', 'gpd']
}

# PArse command line arguments
my_parser = argparse.ArgumentParser(prog=name, description=desc, epilog=epilog)

my_parser.add_argument('game',
                       type=str,
                       help=f"{[x for x in available_games.keys()]}",
                       choices=[x for k in available_games for x in available_games[k]]
                       )

my_parser.add_argument('-s', '--suspense',
                       type=bool,
                       default=False,
                       help="[True, False] (Default: False) Set to True if you desire a more suspensfull tournament",
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

# tournament = Tournament('rock_paper_scissor')
# tournament = Tournament('generalized_prisonners_dilemma', suspense=False)
# tournament.run()