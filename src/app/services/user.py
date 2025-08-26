from .validate import validate_guess, validate_level, validate_part


def get_level():
    while True:
        try:
            level = int(input('Select a difficulty level (1-4): '))
            validate_level(level)
            return level + 3
        except ValueError as e:
            print(f'Invalid input: {e}. Please enter a number between 1 and 4.')


def get_guess(level):
    while True:
        try:
            guess = set_guess(input(f'Guess the {level} digit code: ').split(','))
            validate_guess(guess, level)
            return guess
        except ValueError as e:
            print(f'Invalid input: {e}. Please enter {level} comma separated numerical values.')

def set_guess(guess):
    output = []
    for num in guess:
        validate_part(int(num))
        output.append(int(num))
    return tuple(output)
