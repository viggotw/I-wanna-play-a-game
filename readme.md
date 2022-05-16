# PROGO
Welcome to PROGO, a bot competition environment that allows you to both play games and create your own games.

## Available games
- [Rock Paper Scissor](/games/rock_paper_scissor)
- [Generalized Prisoner's Dilemma](/games/generalized_prisoners_dilemma)

## Play a game
### Start a tournament
1. Select the game you want to play. PROGO currently offer two games:
    - `rock_paper_scissor` (`rps`)
    - `generalized_prisoners_dilemma` (`gpd`)
2. Run the tournament: `python progo.py <game name>` (e.g. `python progo.py rock_paper_scissor`)

If you would like to add some more suspense to your tournament, add `--suspense True` to the command. This will insert several delays into the tournament execution, which can be fun if human-made bots are playing against each other.

### Create your own bot
The structure of the bots may vary from game to game, so be sure to read the `readme.md` file located in the folder for the specific game you would like to play. It is also recommended to use one of the demo-bots as a starting-point when creating your own bot.
1. All bots are located in the `contestants` folder each game
2. Copy one of the bots and give it a name of your choice (e.g. `<your name>.py`)

### Verify that your bot is configure properly using unittests
If you are playing a tournament with lots of new bots, it is recommended to run the unit tests first. This will test that all bots output theexpected data. This is especially true if you plan to execute the tournamen with the `suspense` flag set to true, as it is really boring to discover thata bot is not working properly, halfway through the tournament.

Run the unit tests as follows:
`python -m unittest discover`

## Create your own game rules
1. Create a new folder in the `games` folder and give it the name of your game
2. Create a new folder inside your newly created folder called `contestants`. This is where your bots should be placed.
3. Create a `game_environment.py` file with a class that inherits from `GameEnvironmentGeneral`. Implement the game rules in the `get_reward`-method. (Feel free to use one of the existing games as a starting-point. The `rock_paper_scissor` might be the easiest place to start)
4. Create some bots that you place in the `contestants` folder.
5. (Optional) It can be usefull to test the behaviour of the bots before running an actual tournament. Tests are placed in the `tests` folder.
6. If you want to use the command line interface to execute a tournament with your game, you must maually add it in `progo.py`
