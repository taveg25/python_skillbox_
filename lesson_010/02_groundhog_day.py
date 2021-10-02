#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.
import random


class IamGoodError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class SuicideError(Exception):
    pass



ENLIGHTENMENT_CARMA_LEVEL = 777
days_exc = [IamGoodError('Зазнался'), DrunkError('Набухался'), CarCrashError('Разбился на тачке'),
            GluttonyError('Обожрался'), DepressionError('Приуныл'), SuicideError('Суицид')]

def one_day():
    karma = random.randint(1, 7)
    if random.randint(1, 13) == 13:
        now_exc = random.choice(days_exc)
        raise now_exc
    return karma

days = 0
self_karma = 0
print ('Начался день сурка')
while self_karma < ENLIGHTENMENT_CARMA_LEVEL:
    try:
        karma = one_day()
        self_karma += karma
    except Exception as exc:
            print(f'карма - {self_karma} событие {exc}')
            # with open('log_day.txt', 'a') as file:
            #     file.write(f'карма - {self_karma} событие {exc} \n')
    days += 1

# with open('log_day.txy', 'a') as file:
#     file.write(f'День сурка кончился, всего дней прошло в дне сурка {days} \n')
print(f'День сурка кончился, всего дней прошло в дне сурка {days}')
