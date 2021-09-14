#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from random import randint

_number = ''
_course_of_game = 0

def some_number():
    '''Загадываем случайное число'''
    global _number
    while len(_number) < 4:
        if len(_number) == 0:
            num = randint(1, 9)
        else:
            num = randint(0, 9)
            if str(num) in _number:
                continue
        _number += str(num)

def check_number(user_number):
    global _course_of_game
    bulls = 0
    cows = 0
    _course_of_game += 1
    for i in range(4):
        if user_number[i] == _number[i]:
            bulls += 1
        elif user_number[i] in _number:
            cows +=1
    dict_result = {'bulls': bulls, 'cows': cows}
    return dict_result

def shaw_number(result):
    # print(_number)
    print('bulls = ', result['bulls'], ', cows = ', result['cows'], ', course os game =', _course_of_game)

def is_gameover(result):
    return result['bulls'] == 4