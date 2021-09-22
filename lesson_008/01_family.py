#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint

######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House(object):

    def __init__(self, money=100, food_for_man=50, mud=0, food_for_cat=30):
        self.money = money
        self.food_for_man = food_for_man
        self.food_for_cat = food_for_cat
        self.mud = mud

    def __str__(self):
        return 'В доме денег осталось {}, еды для людей осталось {}, еды для котов осталось {}' \
               ' уровень грязи составляет {}.'\
            .format(self.money, self.food_for_man, self. food_for_cat, self.mud)


class Man(object):
    count = 0
    eating_food = 0
    petting_cat = 0

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.happy = 100
        self.house = None
        self.spouse = None
        Man.count += 1

    def __str__(self):
        return 'Я - {}, сытость {}, счастье {}'.format(
            self.name, self.fullness, self.happy)

    def wedding(self, name):
        self.spouse = name

    def eat(self):
        if self.house.food_for_man >= 30:
            cprint('{} поел 30'.format(self.name), color='yellow')
            self.fullness += 40
            self.house.food_for_man -= 30
            Man.eating_food += 30
        elif self.house.food_for_man >= 20:
            cprint('{} поел 20'.format(self.name), color='yellow')
            self.fullness += 30
            self.house.food_for_man -= 20
            Man.eating_food += 30
        elif self.house.food_for_man >= 10:
            cprint('{} поел 20'.format(self.name), color='yellow')
            self.fullness += 20
            self.house.food_for_man -= 10
            Man.eating_food += 30
        else:
            cprint('{} нет еды!'.format(self.name), color='red')

    def act(self):
        if (self.fullness <= 0) or (self.happy < 10):
            self.fullness = 0
            cprint('{} умер...'.format(self.name), color='red')
            return
        self.fullness -= 10
        self.house.mud += 5 / Man.count
        if self.house.mud > 90:
            self.happy -= 10



    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def petting_the_cat(self):
        self.happy += 5
        Man.petting_cat += 1
        cprint('{} Погладил кота'.format(self.name), color='cyan')

    def take_cat(self, cat):
        cat.house = self.house
        cprint('{} Вьехал в дом'.format(cat.name), color='cyan')


class Husband(Man):
    money_earned = 0
    gaming_days = 0

    def __init__(self, name):
        super().__init__(name=name)

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.happy -= 7
        Husband.money_earned += 150

    def gaming(self):
        cprint('{} играл целый день'.format(self.name), color='green')
        self.happy += 20
        self.spouse.happy += 5
        Husband.gaming_days += 1

    def act(self):
        super().act()
        if self.fullness > 0:
            dice = randint(1, 6)
            if self.fullness <= 20:
                self.eat()
            elif self.house.money < 100:
                self.work()
            elif dice == (1 or 2):
                self.work()
            elif dice == 3:
                self.eat()
            elif dice == 4:
                self.petting_the_cat()
            else:
                self.gaming()


class Wife(Man):
    fur_coat = 0

    def shopping_for_man(self):
        if self.house.money >= 90:
            cprint('{} сходила в магазин за человеческой едой'.format(self.name), color='magenta')
            self.house.money -= 90
            self.house.food_for_man += 90
            self.happy += 7
        else:
            cprint('{} деньги кончились! Сережа! Срочно на работу'
                   .format(self.name), color='red')
            self.happy -= 30
            self.spouse.happy -= 30

    def shoping_for_cat(self):
        if self.house.money >= 50:
            cprint('{} сходила в магазин за кошачей едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food_for_cat += 50
            self.happy += 3
        else:
            cprint('{}: Сережа деньги кончились! Не сходишь на работу - кот сдохнет!'
                   .format(self.name), color='red')
            self.happy -= 20
            self.spouse.happy -= 20

    def buy_fur_coat(self):
        if self.house.money >= 350:
            cprint('{} сходила в магазин за шубой'.format(self.name), color='red')
            self.house.money -= 350
            self.happy += 60
            Wife.fur_coat += 1
            self.spouse.happy += 30
        else:
            if self.spouse.happy > 100:
                cprint('{}: Сережа, я несчастна, у нас нет денег даже на шубу'
                       .format(self.name), color='red')
                self.spouse.happy -= 50
            else:
                cprint('{}: Сережа, не переживай, потом купим шубу'
                       .format(self.name), color='red')
                self.spouse.happy += 5

    def clean_house(self):
        cprint('{} Убиралась весь день'.format(self.name), color='red')
        if self.house.mud >= 100:
            self.house.mud -= 100
        else:
            self.house.mud = 0

    def act(self):
        super().act()
        if self.fullness > 0:
            dice = randint(1, 6)
            if self.fullness <= 20:
                self.eat()
            elif self.house.food_for_man < 90:
                self.shopping_for_man()
            elif self.house.mud > 110:
                self.clean_house()
            elif self.house.food_for_cat < 70:
                self.shoping_for_cat()
            elif self.happy < 50:
                self.buy_fur_coat()
            elif dice == 1:
                self.clean_house()
            elif dice == 2:
                self.buy_fur_coat()
            elif dice == 3:
                self.shopping_for_man()
            elif dice == 4:
                self.eat()
            else:
                self.petting_the_cat()


class Cat(object):
    cat_mud = 0

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food_for_cat >= 15:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 30
            self.house.food_for_cat -= 15
        else:
            cprint('{}: МЯУ нет кошачей еды'.format(self.name), color='red')
            self.sleep()

    def sleep(self):
        cprint('{} поспал'.format(self.name), color='blue')
        self.fullness -= 10

    def breake_wall(self):
        cprint('{} подрал обои'.format(self.name), color='blue')
        self.fullness -= 10
        self.house.mud += 5
        Cat.cat_mud += 5

    def act(self):
        if self.fullness <= 0 or self.house.mud > 120:
            self.fullness = 0
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 30:
            self.eat()
        elif dice == 1:
            self.breake_wall()
        elif dice == 2:
            self.eat()
        else:
            self.sleep()

home = House()
serge = Husband(name='Сережа')
serge.go_to_the_house(home)
masha = Wife(name='Маша')
masha.go_to_the_house(home)
masha.wedding(serge)
serge.wedding(masha)
barsik = Cat(name='Барсик')
masha.take_cat(barsik)

for day in range(66):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    barsik.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(barsik, color='cyan')
    cprint(home, color='cyan')
cprint('Всего заработано денег {}'.format(Husband.money_earned), color='yellow')
cprint('Всего проиграно дней {}'.format(Husband.gaming_days), color='yellow')
cprint('Всего съедено еды {}'.format(Man.eating_food), color='yellow')
cprint('Всего куплено шуб {}'.format(Wife.fur_coat), color='yellow')
cprint('Кота погладили {} раз (дней)'.format(Man.petting_cat), color='yellow')
cprint('Грязи от кота за период {}'.format(Cat.cat_mud), color='yellow')

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов





######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child:

    def __init__(self):
        pass

    def __str__(self):
        return super().__str__()

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass


# TODO после реализации второй части - отдать на проверку учителем две ветки


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')


# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')

