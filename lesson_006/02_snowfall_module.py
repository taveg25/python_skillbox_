#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import simple_draw as sd
import snowfall
# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

# создать_снежинки(N)
sd.resolution = (1200, 600)
snowfall.create_snow(10)
while True:
    #  нарисовать_снежинки_цветом(color=sd.background_color)
    snowfall.draw_snow(sd.COLOR_WHITE)
    #  сдвинуть_снежинки()
    snowfall.slide_snow()
    #  нарисовать_снежинки_цветом(color)
    snowfall.draw_snow(sd.COLOR_WHITE)
    #  если есть номера_достигших_низа_экрана() то
    if snowfall.number_of_fallen():
        snowfall.del_snow()
        snowfall.create_snow(len(snowfall._number))
    #       удалить_снежинки(номера)
    #       создать_снежинки(count)
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
