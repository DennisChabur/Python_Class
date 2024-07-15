'''
2. В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
'''
import argparse
from datetime import datetime
from sys import argv

__all__ = ['check_year', 'date_validator']

def _check_leap_year(date: str) -> bool:
    CHECK_NORMAL_1 = 4
    CHECK_NORMAL_2 = 100
    CHECK_NORMAL_3 = 400
    YEARS = range(1, 10000)
    year = int(date.split(".")[-1])
    if year in YEARS and year % CHECK_NORMAL_1 == 0 and year % CHECK_NORMAL_2 != 0 or year % CHECK_NORMAL_3 == 0:
        return True
    return False


def check_year(year: str) -> bool:
    try:
        _ = datetime.strptime(year, "%d.%m.%Y").date()
        return True
    except:
        return False


def date_validator(date_for_check: str) -> str:
    if check_year(date_for_check):
        return 'Високосный' if _check_leap_year(date_for_check) else 'Не является високосным'
    else:
        return f'Дата заполнена некорректно'


if __name__ == "__main__":
    if len(argv) == 2:
        _, date = argv
        print(date_validator(date))
    else:
        print("Дата для проверки не указана!")

'''
3. Добавьте в пакет, созданный на семинаре шахматный модуль. 
Внутри него напишите код, решающий задачу о 8 ферзях. 
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. 
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. 
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. 
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
'''

def validate_queens(positions):
    for i in range(8):
        for j in range(i+1, 8):
            # проверка на наличие на одной строке или диагонали
            if positions[i] == positions[j] or \
                positions[i] - i == positions[j] - j or \
                positions[i] + i == positions[j] + j:
                return False
    return True

'''
4. Напишите функцию в шахматный модуль. Используйте генератор случайных чисел 
для случайной расстановки ферзей в задаче выше. Проверяйте различный случайные варианты 
и выведите 4 успешных расстановки.
'''

import random

def generate_positions():
    positions = list(range(1, 9))
    for i in range(4):
        random.shuffle(positions)
        while not validate_queens(positions):
            random.shuffle(positions)
        print(positions)