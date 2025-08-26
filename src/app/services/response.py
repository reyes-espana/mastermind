from .validate import validate_extend
from .db import guesses

from tabulate import tabulate


def view(tries):
    table = print(guesses.view_all())
    attempts = print(f'You have {tries} {'attempts' if tries != 1 else 'attempt'} remaining.')
    return table, attempts

def no_end(score, penalty, tries):
    table, attempts = view(tries)
    score -= penalty
    tries -= 1
    return table, attempts, score, tries

def end(total):
    # TODO: tabulate
    print(f'Final Score: {total}')
    return guesses.reset()

def good_end(score, level):
    res = print(f'You cracked the code! Score: {score}')
    phrase = 'Next Level? (Y/N): ' if level < 5 else 'Play Again? (Y/N): '
    extend = input(f'{phrase}').upper()
    validate_extend(extend)
    guesses.reset()
    return res, extend, score

def bad_end(code, score, total):
    res = print(f'Answer: {code}')
    extend = input('Continue? (Y/N): ').upper()
    validate_extend(extend)
    score, total = 0, 0
    guesses.reset()
    return res, extend, score, total
