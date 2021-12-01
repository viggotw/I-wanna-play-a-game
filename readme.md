# PROGO
PROGO is a platform that allows programmers to select a game, and scipt and submit a contestant that will play against bots or the scripts of other people. Currently, there is only implemented one game: tic-tac-toe.

## Run the game
Before running the game, it is often a good idea to ensure that you have all the required packages installed. Assuming you already have conda installed, run the following command in your terminal from your PROGO-folder
`conda env create --file environment.yml`
When this is done, activate the environment using `activate progo`

To run a game, simply run the `main.py`-file in your terminal
`python main.py`

This will load the contestants from the `games\rock_paper_scissor\contestants`-folder and execute a tournament where several one-vs-one matches will be played.

If you want to submit your own contestant, just create a new python-file in the `contestants`-folder.