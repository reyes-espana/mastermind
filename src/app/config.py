from .services import generate, response, stats, user


def level():
    return user.get_level()


def code(level):
    return generate.get_numbers(level)


def guess(level):
    return user.get_guess(level)


def score(guess, code, level):
    return stats.score_code(guess, code, level)


def no_fin(score, penalty, tries):
    return response.no_end(score, penalty, tries)

def final(total):
    return response.end(total)

def good_fin(score, level):
    return response.good_end(score, level)

def bad_fin(code, score, total):
    return response.bad_end(code, score, total)
