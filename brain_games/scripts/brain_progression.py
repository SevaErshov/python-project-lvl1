#!/usr/bit/env python3
from random import randint
from brain_games.game_logic import game_logic


condition = 'What number is missing in the progression?'


def question():
    diff = randint(1, 10)
    first = randint(1, 25)
    progress = [first]
    for i in range(9):
        progress.append(progress[i] + diff)
    index_answer = randint(0, 9)
    answer = progress[index_answer]
    progress[index_answer] = ".."
    progress = list(map(str, progress))
    question = " ".join(progress)
    return question, str(answer)


def main():
    game_logic(condition, question)


if __name__ == "__main__":
    main()
