# -*- coding: utf-8 -*-

# С помощью JSON файла rpg.json задана "карта" подземелья.
# Подземелье было выкопано монстрами и они всё ещё скрываются где-то в его глубинах,
# планируя набеги на близлежащие поселения.
# Само подземелье состоит из двух главных разветвлений и нескольких развилок,
# и лишь один из путей приведёт вас к главному Боссу
# и позволит предотвратить набеги и спасти мирных жителей.

# Напишите игру, в которой пользователь, с помощью консоли,
# сможет:
# 1) исследовать это подземелье:
#   -- передвижение должно осуществляться присваиванием переменной и только в одну сторону
#   -- перемещаясь из одной локации в другую, пользователь теряет время, указанное в конце названия каждой локации
# Так, перейдя в локацию Location_1_tm500 - вам необходимо будет списать со счёта 500 секунд.
# Тег, в названии локации, указывающий на время - 'tm'.
#
# 2) сражаться с монстрами:
#   -- сражение имитируется списанием со счета персонажа N-количества времени и получением N-количества опыта
#   -- опыт и время указаны в названиях монстров (после exp указано значение опыта и после tm указано время)
# Так, если в локации вы обнаружили монстра Mob_exp10_tm20 (или Boss_exp10_tm20)
# необходимо списать со счета 20 секунд и добавить 10 очков опыта.
# Теги указывающие на опыт и время - 'exp' и 'tm'.
# После того, как игра будет готова, сыграйте в неё и наберите 280 очков при положительном остатке времени.

# По мере продвижения вам так же необходимо вести журнал,
# в котором должна содержаться следующая информация:
# -- текущее положение
# -- текущее количество опыта
# -- текущая дата (отсчёт вести с первой локации с помощью datetime)
# После прохождения лабиринта, набора 280 очков опыта и проверки на остаток времени (remaining_time > 0),
# журнал необходимо записать в csv файл (назвать dungeon.csv, названия столбцов взять из field_names).

# Пример лога игры:
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 1234567890.0987654321 секунд
# Прошло уже 0:00:00 - не ясно что тут имеется ввиду, введем уточнение - будем считать что речь идет о реальном времени
# Внутри вы видите:
# -- Монстра Mob_exp10_tm0
# -- Вход в локацию: Location_1_tm10400000
# -- Вход в локацию: Location_2_tm333000000
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Выход
from decimal import Decimal
import csv
import re
import json
import datetime

remaining_time = '1234567890.0987654321'
# если изначально не писать число в виде строки - теряется точность!
field_names = ['current_location', 'current_experience', 'current_date']

re_location = r'Location.*'
re_mob = r'.*exp.*'
re_exp = r'.*_exp(\d*)_.*'
re_tm = r'.*_tm(\d*.*)'


class Hero(object):
    def __init__(self, name):
        self.name = name
        self.exp = 0
        self.time = Decimal('1234567890.0987654321')
        self.location = "Location_0_tm0"
        self.time_start = datetime.datetime.now()
        with open("rpg.json", "r") as read_file:
            self.data = json.load(read_file)
        self.data_path = "self.data['Location_0_tm0']"
        self.field_names = ['current_location', 'current_experience', 'current_date']
        self.logs = [{self.field_names[0]: self.field_names[0],
                      self.field_names[1]: self.field_names[1],
                      self.field_names[2]: self.field_names[2]}]

    def run(self):
        while True:
            print('-' * 10)
            self.time_pr = (datetime.datetime.now() - self.time_start)
            self.logs.append({self.field_names[0]: self.location,
                              self.field_names[1]: self.exp,
                              self.field_names[2]: self.time_pr})
            print(f'Вы находитесь в {self.location}\n'
                  f'У Вас {self.exp} опыта и осталось {self.time} времени\n'
                  f'Прошло уже {self.time_pr}\n'
                  f'Внутри Вы видете:')
            self.what_show()
            print('Выберите действие:\n'
                  '1 - Kill the monster\n'
                  '2 - Change location\n'
                  '3 - Exit')
            action = input(': ').strip()
            if action == '3':
                self.save_logs()
                break
            elif action == '1':
                if type(self.d) == list:
                    mobs = []
                    for i in self.d:
                        if type(i) == str:
                            mobs.append(i)
                        elif type(i) == list:
                            for j in i:
                                if type(j) == str:
                                    mobs.append(j)
                    if len(mobs) == 0:
                        mob = None
                        print('Monster is absent')
                        continue
                    print('What monster do you want kill?')
                    for j in range(len(mobs)):
                        print(f'{j+1} - {mobs[j]}')
                    action_2 = input(': ').strip()
                    try:
                        mob = mobs[int(action_2)-1]
                        mobs.remove(mob)
                    except BaseException:
                        mob = None
                self.kill_mob(mob)
            elif action == '2':
                locs = []
                self.locs_2 = []
                for i in self.d:
                    if type(i) == dict:
                        for key in i.keys():
                            locs.append(key)
                            self.locs_2.append(i)
                print('What place')
                for j in range(len(locs)):
                    print(f'{j + 1} - {locs[j]}')
                action_3 = input(': ').strip()
                try:
                    loc = locs[int(action_3) - 1]
                    self.add_path = '[' + str(self.d.index(self.locs_2[int(action_3) - 1])) + ']["' + loc + '"]'
                    print(self.add_path)
                except BaseException:
                    loc = None
                self.change_location(loc)
            else:
                print('<Unknown command>')

    def what_show(self):
        self.d = eval(self.data_path)
        for x in (self.d):
            if type(x) == str:
                print(x)
            elif type(x) == dict:
                for key in x.keys():
                    print(key)
            elif type(x) == list:
                for t in x: print(t)
        print(type(self.d))

    def kill_mob(self, mob):
        if mob:
            exp = int(re.search(re_exp, mob)[1])
            self.exp += exp
            tm = Decimal(re.search(re_tm, mob)[1])
            self.time -= tm
            try:
                self.d.remove(mob)
            except BaseException:
                self.d[0].remove(mob) #Это, конечно, костыль, нужно более универсально делать
                print('net')

        else:
            print('Monster is absent(kill bot)')

    def change_location(self, loc):
        tm = Decimal(re.search(re_tm, loc)[1])
        self.time -= tm
        self.location = loc
        self.data_path += self.add_path

    def save_logs(self):
        with open('dungeon.csv', "a", newline='') as out_file:
            writer = csv.DictWriter(out_file, delimiter=',', fieldnames=self.field_names)
            for one_log in self.logs:
                writer.writerow(one_log)

Igor = Hero('Igor')
Igor.run()








# Учитывая время и опыт, не забывайте о точности вычислений!

