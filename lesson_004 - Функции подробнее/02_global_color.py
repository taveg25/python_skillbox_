#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004 - Функции подробнее/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004 - Функции подробнее/results/exercise_02_global_color.jpg

def drawing(point, angle, length, alpha, color):
    v = sd.get_vector(start_point=point, angle=alpha+angle, length=length, width=3, )
    v.draw(color=color)
    return v.end_point


def triangle(point, angle, length, color):
    for alpha in range(0, 241, 120):
        point = drawing(point, angle, length, alpha, color)


def square(point, angle, length, color):
    for alpha in range(0, 271, 90):
        point = drawing(point, angle, length, alpha, color)


def hexagon(point, angle, length, color):
    for alpha in range(0, 301, 60):
        point = drawing(point, angle, length, alpha, color)



dict_colors_user = {'1':'red', '2':'orange',
                    '3':'yellow', '4':'green',
                    '5':'blue', '6':'purple'}
dict_colors_program = {'red':sd.COLOR_RED, 'orange':sd.COLOR_ORANGE,
                       'yellow':sd.COLOR_YELLOW, 'green':sd.COLOR_GREEN,
                       'blue':sd.COLOR_BLUE, 'purple':sd.COLOR_PURPLE}
print('возможные цвета:')
for key, value in dict_colors_user.items():
    print(key, ':', value)
s = input('выберете цвет').strip()
if s in dict_colors_user.keys():
    sd.resolution = (1200, 600)
    color = dict_colors_program[dict_colors_user[s]]
    start_point_triangle = sd.get_point(300, 100)
    start_point_square = sd.get_point(500, 200)
    triangle(start_point_triangle, 30, 200, color=color)
    square(start_point_square, 30, 100, color=color)
    start_point_hexagon = sd.get_point(800, 300)
    hexagon(start_point_hexagon, 0, 150, color=color)

    sd.pause()
else:
    print('Некорректный ввод')
