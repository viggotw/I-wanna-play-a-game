# PROGO: Generalized Prisoner's Dilemma
## Rules
This is a round-robin tournament, where each 1v1 match is played with 100 iterations. The winner is the bot that collects the most points in total.

## Interface (how to create a bot)
The interface is pretty simple, and there is basically only three things you need to know:
1. Write all your code inside the `action`-method.
2. The method must always return one of these three values: `Action.COOPERATE` or `Action.BETRAY`
3. Throughout the match, you have access to a log of the previously played matched using the input `game_log`. This is a dictionary, where the structure is illustrated below. The `'moves'`-lists contain the previously played actions (e.g. `Action.BETRAY-`). Notice how the `opponents` dictionary is in plural. This is because the `game_log` supports games with multiple opponents. This also means that you must index one extra level, compared to the `me` dictionary (e.g. `game_log['me']['moves']` vs. `game_log['opponent']['moves'][0]`)
4. The `game_log` also contains a `board_game` part that will display a payoff matrix. This matrix defines how much point you and the opponent will receive based on your moves this round. You can read the potential payoff in the payoff matrix like this: `game_log[my_action, opponents_action]` (e.g. `game_log[Action.BETRAY, Action.COOPERATE]`).

Here you see an example of the `game_log` input:
```python
{
    'me': {
        'score': 0,
        'moves': []
    },
    'opponents': {
        'score': [0],
        'moves': [[]]
    }
    'game_board': {
        (Action.COOPERATE, Action.COOPERATE): (<int>,<int>)
        (Action.BETRAY,    Action.COOPERATE): (<int>,<int>)
        (Action.COOPERATE,    Action.BETRAY): (<int>,<int>)
        (Action.BETRAY,       Action.BETRAY): (<int>,<int>)
        }
    }
}
```

The payoff matrix can be thought of as follows
```
                                         opponent
             |           Cooperate          |             Betray           |
   ----------|------------------------------|------------------------------|
   Cooperate | <my_score>,<opponents_score> | <my_score>,<opponents_score> |
me ----------|------------------------------|------------------------------|
      Betray | <my_score>,<opponents_score> | <my_score>,<opponents_score> |
   ----------|------------------------------|------------------------------|
```