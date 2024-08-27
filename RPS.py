import random

def player(prev_play, opponent_history=[]):
    if not prev_play:
        # First game, play randomly
        return random.choice(["R", "P", "S"])

    opponent_history.append(prev_play)

    # Analyze opponent's history to determine next move
    if len(opponent_history) > 2:
        # Check for patterns in opponent's history
        patterns = {
            "RR": "P",
            "RP": "S",
            "RS": "R",
            "PR": "S",
            "PP": "R",
            "PS": "P",
            "SR": "R",
            "SP": "P",
            "SS": "S"
        }
        pattern = "".join(opponent_history[-2:])
        if pattern in patterns:
            return patterns[pattern]

    # If no pattern is found, play randomly
    return random.choice(["R", "P", "S"])