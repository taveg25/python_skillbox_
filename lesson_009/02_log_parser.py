# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.


class LogEvents(object):

    def __init__(self, in_file_name, out_file_name):
        self.in_file_name = in_file_name
        self. out_file_name = out_file_name

    def write_NOK(self, prev_line):
        with open(self.out_file_name, 'a') as file:
            if self.count > 0:
                file.write(prev_line[0:17] + ']' + ' ' + str(self.count) + '\n')

    def count_NOK(self, file):
        for line in file:
            if line[0:17] == self.prev_line_NOK[0:17]:
                if 'NOK' in line[-4:]:
                    self.count += 1
                    self.prev_line_NOK = line
                else:
                    continue
            else:
                if 'NOK' in line[-4:]:
                    self.write_NOK(self.prev_line_NOK)
                    self.count = 1
                    self.prev_line_NOK = line
                    continue
                self.write_NOK(self.prev_line_NOK)
                self.count = 0
                self.prev_line_NOK = line

    def read(self):
        self.prev_line_NOK = ' NOK'
        self.count = 0
        with open(self.in_file_name, 'r') as file:
            self.count_NOK(file)


class LogTime(LogEvents):

    def __init__(self, in_file_name, out_file_name, time):
        super().__init__(in_file_name=in_file_name, out_file_name=out_file_name)
        self.time = time

    def times(self, file):
        for line in file:
            if self.time in line[12:14]:
                with open(self.out_file_name, 'a') as file:
                    file.write(line)

    def read(self):
        with open(self.in_file_name, 'r') as file:
            self.times(file)



#
# event = LogEvents('events.txt', 'e.txt')
# event.read()
event2 = LogTime('events.txt', 'e2.txt', time='22')
event2.read()


# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу -делается также как и по часам, не вижу смысла делать - новый класс и переопределение
#  - по году -делается также как и по часам, не вижу смысла делать - новый класс и переопределение
# ну или я не понял шаблонный метод
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
