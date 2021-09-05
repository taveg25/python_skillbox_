#/bin/usr/env python3
# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
sd.resolution = (1200, 600)
x_1, y_1 = 50, 20
x_2, y_2 = 200, 450
step = 10
for _ in range(7):
    start_point = sd.get_point(x_1, y_1)
    end_point = sd.get_point(x_2, y_2)
    color = sd.random_color()
    sd.line(start_point, end_point, color, width=9)
    x_1 += step
    y_1 += step
    x_2 += step
    y_2 += step

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код
x_centr = 600
y_centr = -300
radius = 500
for _ in range(7):
    centr_position = sd.get_point(x_centr, y_centr)
    color = sd.random_color()
    sd.circle(centr_position, radius, color, width=9)
    # x_centr += step
    y_centr += step

sd.pause()
