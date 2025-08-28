from .user import get_extend
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
    guesses.reset()
    res = print(tabulate([["💯 Final Score:",total]], tablefmt="simple"))
    return res

def good_end(score, level):
    res = print(tabulate([["✨ You cracked the code!✨ Score:", score]], tablefmt="simple"))
    extend = get_extend(level)
    guesses.reset()
    return res, extend, score

def bad_end(code, score, total):
    res = print(f'Answer: {code}')
    extend = get_extend(0)
    score, total = 0, 0
    guesses.reset()
    return res, extend, score, total
