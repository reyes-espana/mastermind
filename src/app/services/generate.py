import requests as req
import random


def get_numbers(level):
    try:
        url = f'https://www.random.org/integers/?num={level}&min=0&max=7&col=1&base=10&format=plain&rnd=new'
        res = req.get(url)
        res.raise_for_status() 
        numbers = res.text.strip().split('\n')
        code = tuple(int(num) for num in numbers if num)
        return code
    except req.exceptions.RequestException as e:
        print(f'{e}, falling back to local generation.')
        return get_backup(level)
    except (ValueError, TypeError):
        print('API call failed, falling back to local generation.')
        return get_backup(level)

def get_backup(level):
    code = []
    while level > 0:
        code.append(random.randint(0, 7))
        level -= 1
    return tuple(code)
