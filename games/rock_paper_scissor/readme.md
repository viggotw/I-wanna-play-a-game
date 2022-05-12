# PROGO: Rock Paper Scissor
## Rules
Pretty straight forward. Rock beats Scissor, Scissor beats Paper, and Paper bears Rock. This is a round-robin tournament, where each 1v1 match is played with 100 iterations. The winner is the bot that wins the most matches.

## Interface (how to create a bot)
The interface is pretty simple, and there is basically only three things you need to know:
1. Write all your code inside the `action`-method.
2. The method must always return one of these three values: `Action.ROCK`, `Action.PAPER` or `Action.SCISSOR`.
3. Throughout the match, you have access to a log of the previously played matched using the input `game_log`. This is a dictionary, where the structure is illustrated below. The `'moves'`-lists contain the previously played actions (e.g. `Action.ROCK`). Notice how the `opponents` dictionary is in plural. This is because the `game_log` supports games with multiple opponents. This also means that you must index one extra level, compared to the `me` dictionary (e.g. `game_log['me']['moves']` vs. `game_log['opponent']['moves'][0]`)

```python
game_log = 
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
````