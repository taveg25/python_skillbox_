#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from random import randint

import simple_draw as sd


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake(object):
    count_to_del = 0

    def __init__(self, length=100):
        self.length = length
        self.x = randint(1, 1600)
        self.y = randint(400, 500)
        self.point = None

    def __str__(self):
        return 'x {}, y {}'.format(
            self.x, self.y)

    def clear_previous_picture(self):
        if self.point != None:
            sd.snowflake(self.point, color=sd.background_color)

    def move(self):
        self.y -= 10

    def draw(self):
        self.point = sd.get_point(self.x, self.y)
        sd.snowflake(self.point, self.length)

    def can_fall(self):
        return self.y > 50


def get_flakes(count=5):
    list = []
    for i in range(count):
        flake_in_list = Snowflake()
        list.append(flake_in_list)
    return list


def get_fallen_flakes():
    if not flake.can_fall():
        Snowflake.count_to_del += 1
    return Snowflake.count_to_del


sd.resolution = (1600, 600)
flake = Snowflake()

while True:
    flake.clear_previous_picture()
    flake.move()
    flake.draw()
    if not flake.can_fall():
        break
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# жутко туплю на шаге два - решил его не делать


# создать список снежинок
# flakes = get_flakes(count=10)
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         del flake
#     #     append.flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

sd.pause()
