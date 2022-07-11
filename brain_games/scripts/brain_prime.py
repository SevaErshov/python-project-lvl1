#!/usr/bit/env python3
from random import randint
from brain_games.game_logic import game_logic


condition = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    d = 2
    while number % d != 0:
        d += 1
    return d == number


def question():
    number = randint(1, 99)
    if is_prime(number):
        answer = 'yes'
    else:
        answer = 'no'
    return number, answer


def main():
    game_logic(condition, question)


if __name__ == "__main__":
    main()

