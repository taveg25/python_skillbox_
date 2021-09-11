#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import simple_draw as sd
import random as rd
# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,
def draw_branches(point, angle, length):
    if length < 4:
        return 1
    alpha = 30 * rd.randint(80, 140)/100
    v_1 = sd.get_vector(start_point=point, angle=angle-alpha, length=length, width=1)
    v_2 = sd.get_vector(start_point=point, angle=angle+alpha, length=length, width=1)
    v_1.draw()
    v_2.draw()
    next_point_v_1 = v_1.end_point
    next_point_v_2 =v_2.end_point
    next_angle_v_1 = v_1.angle
    next_angle_v_2 = v_2.angle
    print(next_angle_v_1)
    next_length = length * .75* rd.randint(75, 125)/100
    draw_branches(point=next_point_v_1, angle=next_angle_v_1, length=next_length)
    draw_branches(point=next_point_v_2, angle=next_angle_v_2, length=next_length)

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения


sd.resolution = (1200, 600)
point = sd.get_point(600, 50)
draw_branches(point, 90, 100) #функция вызвана дважды, чтобы удостоверится в верном результате
draw_branches(point, 90, 100)
# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()


