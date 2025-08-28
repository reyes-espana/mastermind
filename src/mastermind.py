from app import config


def main():
    total = 0
    extend = ''
    difficulty = [4, 5, 6,]

    while True: 
        if extend in ('Y', 'YES') and level in difficulty:
            level = level + 1 if total > 0 else level
            code = config.code(level)
            print(code)
            total, extend = game(level, code, total)
        elif extend in ('N', 'NO'): break
        else:
            level = config.level()
            code = config.code(level)
            print(code)
            total, extend = game(level, code, total)

    return config.final(total)


def game(level, code, total):
    extend = ''
    score = 100
    tries = 9

    while True:
        guess = config.guess(level)

        penalty = config.score(guess, code, level)
        if penalty == 0:
            res, extend, score = config.good_fin(score, level)
            break
        elif tries ==  0:
            res, extend, score, total = config.bad_fin(code, score, total)
            break
        else:
            res, attempts, score, tries = config.no_fin(score, penalty, tries)

    score += total
    return score, extend


if __name__ == "__main__":
    main()
