from random import randint
from datetime import datetime


def roll():
    roll = randint(1, 100)
    print(f'User rolled {roll}!')


birthdays = []

def birthday():
    birthday = str(input('Please, type in your birthday! '))
    birthdays.append(birthday)

    if birthday == datetime.now():
        print(f'Happy Birthday! @user >w<
              \nHope you have an awesome day!')
        

