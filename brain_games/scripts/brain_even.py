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
    question = randint(0, 99)
    return question, check_answer(question)


def main():
    game_logic(condition, question)


if __name__ == "__main__":
    main()
