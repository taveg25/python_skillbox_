# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

import zipfile

class CharStat(object):

    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}
        self.all_char = 0
        self.stat_sort_1 = None
        self.stat_sort_abc = None
        self.stat_sort_cba = None

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def static(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        self.all_char += 1
                        if char in self.stat:
                            self.stat[char] += 1
                        else:
                            self.stat[char] = 1
                    else:
                        continue

    def static_sort_number(self):
        self.stat_sort_1 = []
        for char, count in self.stat.items():
            self.stat_sort_1.append([count, char])
        self.stat_sort_1.sort(reverse=True)

    def static_sort_abc(self):
        self.stat_sort_abc = []
        for char, count in self.stat.items():
            self.stat_sort_abc.append([char, count])
        self.stat_sort_abc.sort()

    def static_sort_cab(self):
        self.stat_sort_cba = []
        for char, count in self.stat.items():
            self.stat_sort_cba.append([char, count])
        self.stat_sort_cba.sort(reverse=True)

    def prin(self, sort):
        if sort == 'number':
            for i in self.stat_sort_1:
                print('+', '-' * 8, '+', '-' * 8, '+')
                print('|{txt:^10}|{txt2:^10}| '.format(txt=i[1], txt2=i[0]))
            print('+', '-' * 8, '+', '-' * 8, '+')
            print('|{txt:^10}|{txt2:^10}| '.format(txt='Итого', txt2=self.all_char))
            print('+', '-' * 8, '+', '-' * 8, '+')
        elif sort == 'abc':
            for i in self.stat_sort_abc:
                print('+', '-' * 8, '+', '-' * 8, '+')
                print('|{txt:^10}|{txt2:^10}| '.format(txt=i[0], txt2=i[1]))
            print('+', '-' * 8, '+', '-' * 8, '+')
            print('|{txt:^10}|{txt2:^10}| '.format(txt='Итого', txt2=self.all_char))
            print('+', '-' * 8, '+', '-' * 8, '+')
        elif sort == 'cab':
            for i in self.stat_sort_cba:
                print('+', '-' * 8, '+', '-' * 8, '+')
                print('|{txt:^10}|{txt2:^10}| '.format(txt=i[0], txt2=i[1]))
            print('+', '-' * 8, '+', '-' * 8, '+')
            print('|{txt:^10}|{txt2:^10}| '.format(txt='Итого', txt2=self.all_char))
            print('+', '-' * 8, '+', '-' * 8, '+')
        else:
            print('Выбран неверный метод сортировки')



war = CharStat(file_name='/home/student/PycharmProjects/python_bases/lesson_009/python_snippets/pushkin_cp1251.txt')
war.static()
war.static_sort_number()
war.prin(sort='number')

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
