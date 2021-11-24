#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import simple_draw as sd
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
_x = []
_y = []
_number = []
def create_snow(N):
    global _x
    global _y
    for i in range(N):
        _x.append(sd.random_number(0, 1200))
        _y.append(sd.random_number(400, 600))




def draw_snow(color):
    for i in range(len(_x)):
        point = sd.get_point(_x[i], _y[i])
        sd.snowflake(point, color = color)

# def clear_snow():
#     for i in range(len(_x)):
#         point = sd.get_point(_x[i], _y[i])
#         sd.snowflake(point, color = sd.background_color)

def slide_snow():
    for i in range(len(_x)):
        point = sd.get_point(_x[i], _y[i])
        sd.snowflake(point, color=sd.background_color)
        _y[i] -= 10

def number_of_fallen():
    global _number
    _number = []
    for i in range(len(_x)):
        if _y[i] < 0:
            point = sd.get_point(_x[i], _y[i])
            sd.snowflake(point, color=sd.background_color)
            _number.append(i)
    return _number

def del_snow():
    for i in _number:
        del _x[i]
        del _y[i]
# sd.resolution = (1200, 600)
# create_snow(5)
# draw_snow(sd.COLOR_WHITE)
# sd.sleep(1)
# delete_snow()
#
# slide_snow()
# draw_snow(sd.COLOR_WHITE)
# sd.pause()

