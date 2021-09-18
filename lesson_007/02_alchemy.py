#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава
class Water(object):

    def __init__(self):
        self.name = 'Water'

    def __add__(self, other):
        if type(other) == Wind:
            new_obj = Storm()
        elif type(other) == Fire:
            new_obj = Par()
        elif type(other) == Land:
            new_obj = Mud()
        else:
            new_obj = None
        return new_obj


class Wind(object):

    def __init__(self):
        self.name = 'Wind'

    def __add__(self, other):
        if type(other) == Water:
            new_obj = Storm()
        elif type(other) == Fire:
            new_obj = Par()
        elif type(other) == Land:
            new_obj = Mud()
        else:
            new_obj = None
        return new_obj


class Fire(object):

    def __init__(self):
        self.name = 'Fire'

    def __add__(self, other):
        if type(other) == Water:
            new_obj = Par()
        elif type(other) == Wind:
            new_obj = Lighting()
        elif type(other) == Land:
            new_obj = Lava()
        else:
            new_obj = None
        return new_obj


class Land(object):

    def __init__(self):
        self.name = 'Land'

    def __add__(self, other):
        if type(other) == Water:
            new_obj = Mud()
        elif type(other) == Wind:
            new_obj = Dust()
        elif type(other) == Fire:
            new_obj = Lava()
        else:
            new_obj = None
        return new_obj


class Storm(object):
    def __init__(self):
        self.name = 'Storm'
    def __str__(self):
        return 'I am Storm'

class Par(object):
    def __init__(self):
        self.name = 'Par'
    def __str__(self):
        return 'I am Par'


class Mud(object):
    def __init__(self):
        self.name = 'Mud'
    def __str__(self):
        return 'i am' + ' '+ self.name

class Lighting(object):
    def __init__(self):
        self.name = 'Lighting'

class Dust(object):
    def __init__(self):
        self.name = 'Lighting'

    def __str__(self):
        return 'I am Dust'

class Lava(object):
    def __init__(self):
        self.name = 'Lava'

    def __str__(self):
        return 'I am Lava'

#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава
a = Water()
b = Wind()
c = Fire()
d = Land()
print(Water == type(a))
print(a + c)

