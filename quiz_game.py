"""
Name = Ye Min Aung
Date = 10 / 1 / 2022
Project name = quiz game
"""

import time

def start_quiz():
    questions = {
        'CPU': 'central processing unit',
        'GPU': 'graphics processing unit',
        'RAM': 'random access memory',
        'HDD': 'hard disk drive',
        'SSD': 'solid state drive',
    }

    marks = 0
    question_count = 0
    quiz_answers = []

    print('Answer below questios as short as possible\n')

    for question in questions.keys():
        user_answer = input(f'What does {question} stand for? : ')
        quiz_answers.append(user_answer)

    print('\nWe are checking your answers....\n')
    time.sleep(2)

    for user_answer, quiz_answer in zip(quiz_answers, questions.values()):
        question_count += 1
        if user_answer.lower() == quiz_answer:
            print(f'Question {question_count} -> Correct')
            marks += 1
            time.sleep(1.5)
        else:
            print(f'Question {question_count} -> Incorrect!')
            time.sleep(1.5)
    print(f'\nYou got {marks}/{question_count} marks in this Computer Quiz!')


def run_test():
    print('Welcome to Computer Quiz!')

    playing = input('Do you want to play? : ')

    if playing != 'yes':
        quit('Bye..Bye..')
    else:
        print('Let\'s Play!...')
        time.sleep(1)
        start_quiz()

run_test()