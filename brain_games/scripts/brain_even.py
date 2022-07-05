#!/usr/bit/env python3
from random import randint
import prompt


def check_answer(question):
    if not question % 2:
        return 'yes'
    else:
        return 'no'


def correct_answer(answer, correct):
    print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < 3:
        question = randint(0, 101)
        print(f'Question: {question}')
        answer = input('Your answer: ')
        correct_answ = check_answer(question)
        if correct_answ == answer:
            print('Correct!')
            count += 1
        else:
            correct_answer(answer, correct_answ)
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()
