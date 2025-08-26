from app import config


def main():
    total = 0
    extend = ''
    
    while True: 
        if len(extend) > 0 and level < 5:
            if extend in ('Y', 'YES'):
                level = level + 1 if total > 0 else level
                code = config.code(level)
                # TODO: remove print()
                print(code) 
                total, extend = game(level, code, total)
            else: break
        else:
            level = config.level()
            code = config.code(level)
            # TODO: remove print()
            print(code) 
            total, extend = game(level, code, total)

    config.final(total)
    return


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
