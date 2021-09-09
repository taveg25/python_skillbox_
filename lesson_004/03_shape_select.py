#!usr/bin/env python3
# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

def drawing(point, angle, length, alpha,):
    v = sd.get_vector(start_point=point, angle=alpha+angle, length=length, width=3, )
    v.draw()
    return v.end_point


def triangle(point, angle, length,):
    for alpha in range(0, 241, 120):
        point = drawing(point, angle, length, alpha,)


def square(point, angle, length,):
    for alpha in range(0, 271, 90):
        point = drawing(point, angle, length, alpha,)


def hexagon(point, angle, length,):
    for alpha in range(0, 301, 60):
        point = drawing(point, angle, length, alpha,)


dict_figures_user = {'1': 'triangle', '2': 'square',
                    '3': 'hexagon',}

dict_figures_program = {'1':triangle,
                       '2': square,
                       '3': hexagon, }
print('возможные фигуры:')
for key, value in dict_figures_user.items():
    print(key, ':', value)
s = input('выберете фигуры').strip()
if s in dict_figures_program.keys():
    sd.resolution = (1200, 600)
    start_point = sd.get_point(500, 200)
    dict_figures_program[s](start_point, 0, 200)
    sd.pause()
else:
    print('Некорректный ввод')

sd.pause()
