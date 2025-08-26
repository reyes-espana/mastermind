
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


def validate_extend(extend):
    ...


def validate_sql(sql):
    ...
