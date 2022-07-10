import prompt


def ask_name():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def fail(answer, correct, name):
    print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")
    print(f"Let's try again, {name}!")


def game_logic(condition, func_question, func_answer):
    name = ask_name()
    print(condition)
    count = 0
    while count < 3:
        question = func_question()
        correct_answ = func_answer(question)
        print(f'Question: {question}')
        answer = input('Your answer: ')
        if correct_answ == answer:
            print('Correct!')
            count += 1
        else:
            fail(answer, correct_answ, name)
            break
    if count == 3:
        print(f'Congratulations, {name}!')