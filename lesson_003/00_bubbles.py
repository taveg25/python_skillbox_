# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import simple_draw as sd
import random

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей

point = sd.get_point(100, 100)
rad = 50
for _ in range(3):
    sd.circle(point, rad)
    rad -= 5

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг

def point_booble(x, y, rad=50, step=2):
    point = sd.get_point(x,y)
    for _ in range(3):
        sd.circle(point, rad, color)
        rad -=step
#проверка работы функции
#point_booble(400, 250, 50, 10)

def random_point_booble(count):
    for _ in range (count):
        point = sd.random_point()
        rad = random.randint(80, 150)
        step = random.randint(5,10)
        for _ in range(3):
            color = sd.random_color()
            sd.circle(point, rad, color)
            rad -=step
# Нарисовать 10 пузырьков в ряд

# for x in range(100, 1001, 100):
#     point_booble(x, 200)
# Нарисовать три ряда по 10 пузырьков

# for y in range(200,500, 110):
#     for x in range(100,1101,110):
#         point_booble(x,y)
# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# Чтобы сделать все красиво, ввел функцию
random_point_booble(100)
sd.pause()
