
def validate_level(level):
    if not level:
        raise ValueError('Numerical value is required')
    if not isinstance(level, int):
        raise ValueError('Numerical value is required')
    if level < 1:
        raise ValueError('Value must be greater than 0')
    if level > 4:
        raise ValueError('Value must be less than 5')


def validate_guess(guess, level):
    if not guess:
        raise ValueError('No input')
    if len(guess) < level:
        raise ValueError('Insufficient values')
    if len(guess) > level:
        raise ValueError('Too many values')

def validate_part(part):
    if not isinstance(part, int):
        raise ValueError('All values must be between 0 and 7')
    if part < 0 or part > 7:
        raise ValueError('All values must be between 0 and 7')
    

def validate_score(guess, code, level):
    if not guess:
        raise TypeError('No guess provided')
    if not code:
        raise TypeError('No code provided')
    if not level:
        raise TypeError('No level provided')
    if len(guess) != len(code):
        raise ValueError('Guess and code must be the same length')


def validate_extend(extend):
    if not extend:
        raise ValueError('No input')
    if not isinstance(extend, str):
        raise TypeError(f'Expected str value, but got {extend}')
    if extend not in ('Y', 'YES', 'N', 'NO'):
        raise ValueError(f'Expected Yes or No, but got {extend}')


def validate_sql(sql):
    ...
