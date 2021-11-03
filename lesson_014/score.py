# -*- coding: utf-8 -*-

# Вас взяли на работу в молодой стартап. Идея стартапа - предоставлять сервис расчета результатов игр.
# Начать решили с боулинга, упрощенной версии.
#
# Правила такие.
#
# Всего 10 кеглей. Игра состоит из 10 фреймов. В одном фрейме до 2х бросков, цель - сбить все кегли.
# Результаты фрейма записываются символами:
#   «Х» – «strike», все 10 кеглей сбиты первым броском
#   «<число>/», например «4/» - «spare», в первый бросок сбиты 4 кегли, во второй – остальные
#   «<число><число>», например, «34» – в первый бросок сбито 3, во второй – 4 кегли.
#   вместо <число> может стоять прочерк «-», например, «-4» - ни одной кегли не было сбито за бросок (первый или второй)
# Результат игры – строка с записью результатов фреймов. Символов-разделителей между фреймами нет.
# Например, для игры из 3 фреймов запись результатов может выглядеть так:
#   «Х4/34»
# Предлагается упрощенный способ подсчета количества очков:
#   «Х» – 20 очков, «4/» - 15 очков, «34» – сумма 3+4=7
# То есть для игры «Х4/34» сумма очков равна 20+15+7=42
#
# Надо написать python-модуль (назвать bowling), предоставляющий API расчета количества очков:
# функцию get_score, принимающую параметр game_result. Функция должна выбрасывать исключения,
# когда game_result содержит некорректные данные. Использовать стандартные исключения по максимуму,
# если не хватает - создать свои.
#
# Обязательно написать тесты на этот модуль. Расположить в папке tests.

# Из текущего файла сделать консольную утилиту для определения количества очков, с помощью пакета argparse
# Скрипт должен принимать параметр --result и печатать на консоль:
#   Количество очков для результатов ХХХ - УУУ.
import re
import argparse

# game_result = '55X4/34X'
regex = "^[1-9xX/-]+$"
parser = argparse.ArgumentParser()
parser.add_argument('game_result', help='result of game')
args = parser.parse_args()

def get_score(game_result):
    game_result_up = game_result.upper()
    kol = game_result_up.count('X')
    kol_2 = game_result_up.count('/')
    check_result(game_result_up, kol)
    if re.search(regex, game_result_up):
        return calculation(game_result_up, kol, kol_2)
    else:
        raise BaseException('Error in date')


def check_result(game_result_up, kol):
    if type(game_result_up) is not str:
        raise BaseException('It is not str')
    elif ((len(game_result_up) - kol) % 2) != 0:
        raise BaseException('It is not str - ne to kolichestvo')


def calculation(game_result_up, kol, kol_2):
    sum = 0
    for i in range(len(game_result_up)):
        if game_result_up[i] == 'X':
            sum += 20
        elif game_result_up[i] == '/':
            if game_result_up[i - 1] == 'X' or i == -1:
                raise BaseException('Tak ne bivaet, input error')
            elif game_result_up[i - 1] != '-':
                sum -= int(game_result_up[i - 1])
            sum += 15
        else:
            if game_result_up[i] == '-':
                sum += 0
            else:
                sum += int(game_result_up[i])
        if sum >= (kol * 20 + kol_2 * 15 + (len(game_result_up) - kol - 2 * kol_2) * 5):
            raise BaseException('Tak ne bivaet, input error, kegley menshe ')
    return f'Количество очков для результатов {game_result_up} - {sum}'


print(get_score(args.game_result))

# При написании кода помнить, что заказчик может захотеть доработок и новых возможностей...
# И, возможно, вам пригодится паттерн проектирования "Состояние",
#   см https://clck.ru/Fudd8 и https://refactoring.guru/ru/design-patterns/state
