#!/usr/bit/env python3
from random import randint
from brain_games.game_logic import game_logic


condition = 'What is the result of the expression?'


def sum_numbers(first, second):
    return first + second


def multiply_numbers(first, second):
    return first * second


def diff_numbers(first, second):
    return first - second


def question():
    operations = {
        '+': sum_numbers,
        '*': multiply_numbers,
        '-': diff_numbers
    }
    oper_symbols = list(operations.keys())

    first, second = randint(1, 20), randint(1, 20)
    operation = randint(0, 2)
    oper_symbol = oper_symbols[operation]
    answer = operations[oper_symbol](first, second)
    return f'{first} {oper_symbols[operation]} {second}', str(answer)


def main():
    game_logic(condition, question)


if __name__ == "__main__":
    main()
