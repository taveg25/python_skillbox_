#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd
import random
# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.


COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_ORANGE = (255, 127, 0)
COLOR_YELLOW = (255, 255, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_CYAN = (0, 255, 255)
COLOR_BLUE = (0, 0, 255)
COLOR_PURPLE = (255, 0, 255)
COLOR_DARK_YELLOW = (127, 127, 0)
COLOR_DARK_ORANGE = (127, 63, 0)
COLOR_DARK_RED = (127, 0, 0)
COLOR_DARK_GREEN = (0, 127, 0)
COLOR_DARK_CYAN = (0, 127, 127)
COLOR_DARK_BLUE = (0, 0, 127)
COLOR_DARK_PURPLE = (127, 0, 127)

def smile(x, y, color = COLOR_YELLOW):
    x_centr = x
    y_centr = y
    radius = 50
    centr_position = sd.get_point(x_centr, y_centr)
    sd.circle(centr_position, radius, color=color, width=0)
    right_eye_position = sd.get_point(x_centr + 25, y_centr + 20)
    left_eye_position = sd.get_point(x_centr - 25, y_centr + 20)
    right_month_position = sd.get_point(x_centr + 15, y_centr - 20)
    left_month_position = sd.get_point(x_centr - 15, y_centr - 20)
    sd.circle(left_eye_position, 10, sd.COLOR_BLACK, width=0)
    sd.circle(right_eye_position, 10, sd.COLOR_BLACK, width=0)
    sd.line(right_month_position, left_month_position, sd.COLOR_BLACK, width=10)

sd.resolution = (1200, 600)
for _ in range(10):
    x = random.randint(50, 1150)
    y = random.randint(50, 550)
    smile(x, y, COLOR_RED)

sd.pause()
