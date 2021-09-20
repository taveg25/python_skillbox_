#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint
from termcolor import cprint

class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food_for_man >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food_for_man -= 10
        else:
            cprint('{} нет еды! Иду в магазин'.format(self.name), color='red')
            self.shopping_for_man()

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping_for_man(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за человеческой едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food_for_man += 50
        else:
            cprint('{} деньги кончились! Пошел на работу'.format(self.name), color='red')
            self.work()

    def shopping_for_cat(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за кошачей едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food_for_cat += 50
        else:
            cprint('{} деньги кончились! Пошел на работу!'.format(self.name), color='red')
            self.work()

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def take_cat(self, cat):
        cat.house = self.house
        cprint('{} Вьехал в дом'.format(cat.name), color='cyan')

    def clean(self):
        self.house.mud -= 100
        self.fullness -= 20

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness <= 20:
            self.eat()
        elif self.house.food_for_man < 20:
            self.shopping_for_man()
        elif self.house.food_for_cat < 120:
            self.shopping_for_cat()
        elif self.house.mud >= 50:
            self.clean()
        elif self.house.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()


class House:

    def __init__(self):
        self.food_for_man = 50
        self.food_for_cat = 30
        self.mud = 0
        self.money = 0

    def __str__(self):
        return 'В доме человеческой еды осталось {}, кошачей еды осталось {}, уровень грязи составляет ' \
               '{} денег осталось {}'.format(
            self.food_for_man, self.food_for_cat, self.mud, self.money)

class Cat(object):

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food_for_cat >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 20
            self.house.food_for_cat -= 10
        else:
            cprint('{} нет кошачей еды'.format(self.name), color='red')
            self.sleep()

    def sleep(self):
        cprint('{} поспал'.format(self.name), color='blue')
        self.fullness -= 10

    def breake_wall(self):
        cprint('{} подрал обои'.format(self.name), color='blue')
        self.fullness -= 10
        self.house.mud += 5

    def act(self):
        if self.fullness <= 0 or self.house.mud > 120:
            self.fullness = 0
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif dice == 1:
            self.breake_wall()
        elif dice == 2:
            self.eat()
        else:
            self.sleep()

leha = Man(name='Лёха')
cats = [Cat(name='Барсик'),
        Cat(name='Матроскин'),
        Cat(name='Мурзик'),
        Cat(name='Васька'),
        Cat(name='Филька'),
        Cat(name='Maks'),
        Cat(name='Begemot'),
        Cat(name='Kot'),
        Cat(name='Koshka'),
        Cat(name='kotenok'),
        ]
my_sweet_home = House()
leha.go_to_the_house(house=my_sweet_home)
for cat in cats:
    leha.take_cat(cat)




for day in range(1, 106):
    print('================ день {} =================='.format(day))
    leha.act()
    for cat in cats:
        cat.act()

    print('--- в конце дня ---')
    print(leha)
    for cat in cats:
        print(cat)
    print(my_sweet_home)


# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.



# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
