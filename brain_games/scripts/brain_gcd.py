#!/usr/bit/env python3
from random import randint
from brain_games.game_logic import game_logic


condition = 'Find the greatest common divisor of given numbers.'


def gcd(*args):
    min_number = min(args)
    first, second = args
    for i in range(min_number, 0, -1):
        if not first % i and not second % i:
            return i


def question():
    random_gcd = randint(1, 5)
    first = randint(1, 30) * random_gcd
    second = randint(1, 30) * random_gcd
    answer = gcd(first, second)
    return f'{first} {second}', str(answer)


def main():
    game_logic(condition, question)


if __name__ == "__main__":
    main()
