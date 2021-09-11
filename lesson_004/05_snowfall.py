#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import simple_draw as sd


# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные


# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

def snowflake_drop(N):
    x, y = [], []
    length_rd = []
    speed =[]
    for i in range(N):
        x.append(sd.random_number(0, 1200))
        y.append(sd.random_number(400, 600))
        length_rd.append(sd.random_number(10, 100))
        speed.append(sd.random_number(-30, 30))

    while True:
        sd.clear_screen()
        for i in range(N):
            point = sd.get_point(x[i], y[i])
            length = length_rd[i]

            sd.snowflake(center=point, length=length)
            y[i] -= 10
            if y[i] < 50:
                break
            # x[i] = x[i] + speed[i] каждая с рандомной скоростью
            x[i] = x[i] + sd.random_number(-30, 30)
        sd.sleep(0.1)
        if sd.user_want_exit():
            break



sd.resolution = (1200, 600)
snowflake_drop(20)

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


