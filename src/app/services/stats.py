from .validate import validate_score
from .db import guesses
from math import ceil


def score_code(guess, code, level):
    validate_score(guess, code, level)
    temp_guess = []
    temp_code = []
    correct = 0
    close = 0
    penalty = 0

    if guess == code:
        return penalty

    for g, c in zip(guess, code):
        if g != c:
            penalty += (10 / level) / 2
            temp_guess.append(g)
            temp_code.append(c)
        else:
            correct += 1

    for num in temp_guess:
        if num not in temp_code:
            penalty += (10 / level) / 2
        else:
            temp_code.remove(num)
            close += 1

    guesses.store(guess, correct, close)
    return int(ceil(penalty))
