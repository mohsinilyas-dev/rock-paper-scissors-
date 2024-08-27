
### Implementation Details

The `RPS.py` file contains a `player` function designed to accept a string input representing the opponent's previous move ("R", "P", or "S"). The function is expected to return a string indicating its next move ("R", "P", or "S").

In the first round of a match, the `player` function receives an empty string, as no previous moves exist.

The `RPS.py` file provides a sample function for you to modify. This function is defined with two parameters: `player(prev_play, opponent_history=[])`. Although the second parameter is optional and not used when the function is called, it is included to enable state persistence between consecutive calls, allowing you to track the opponent’s move history. The `opponent_history` parameter is only necessary if you wish to record the opponent's moves.

### Development

Please refrain from modifying `RPS_game.py`. All code changes should be made within `RPS.py`. For testing purposes, utilize `main.py`, which imports the game function and bots from `RPS_game.py`.

To test, use the `play` function, which requires the following four arguments:

- Two player functions to compete against each other
- The number of games to be played in the match
- An optional argument to log each game (set to `True` for detailed output)

For example, to simulate a match where `player` competes against `quincy` for 1,000 games with detailed logging, use:

```python
play(player, quincy, 1000, verbose=True)
```

### Testing

Unit tests are provided in `test_module.py` and are imported into `main.py` for convenience. To automatically run the tests whenever you execute `python main.py`, simply uncomment the last line in `main.py`.
