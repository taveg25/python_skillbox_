# -*- coding: utf-8 -*-

import simple_draw as sd


# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.

def draw(point, angle, length, alpha):
    v = sd.get_vector(start_point=point, angle=alpha + angle, length=length, width=3)
    v.draw()
    return v.end_point


def triangle(point, angle, length):
    for alpha in range(0, 241, 120):
        point = draw(point, angle, length, alpha)


def square(point, angle, length):
    for alpha in range(0, 271, 90):
        point = draw(point, angle, length, alpha)


def hexagon(point, angle, length):
    for alpha in range(0, 301, 60):
        point = draw(point, angle, length, alpha)


ops = {3: triangle,
       4: square,
       6: hexagon}


def get_polygon(n):
    def draw_selfangle(*args, **kwargs):
        result = ops[n](*args, **kwargs)
        return result
    return draw_selfangle


draw_triangle = get_polygon(n=3)
draw_triangle(point=sd.get_point(200, 200), angle=13, length=100)

sd.pause()
