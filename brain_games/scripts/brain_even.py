#!/usr/bit/env python3
from random import randint
from brain_games.game_logic import game_logic


condition = 'Answer "yes" if the number is even, otherwise answer "no".'


def check_answer(question):
    if not question % 2:
        return 'yes'
    else:
        return 'no'


def question():
    return randint(0, 101)


def main():
    game_logic(condition, question, check_answer)


if __name__ == "__main__":
    main()
