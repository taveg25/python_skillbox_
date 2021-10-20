# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПРОЦЕССНОМ стиле
#
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
import multiprocessing
import os
import csv
import time
from decimal import Decimal


def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()

        result = func(*args, **kwargs)

        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'Функция работала {elapsed} секунд(ы)')
        return result
    return surrogate


class Violatility(multiprocessing.Process):

    def __init__(self, file, collector, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file = file
        global dict_violatility
        global nul
        dict_violatility = {}
        nul = []
        self.collector = collector

    def run(self):
        with open(self.file, 'r', encoding='utf8') as ff:
            file_reader = csv.reader(ff)
            coin_list = []
            number_row = 0
            for row in file_reader:
                number_row += 1
                if number_row > 1:
                    coin_list.append(Decimal(row[2]))
            max_coin = Decimal(max(coin_list))
            min_coin = Decimal(min(coin_list))
            average_price = Decimal((max_coin + min_coin) / 2)
            volatility = Decimal(((max_coin - min_coin) / average_price) * 100)
            dict_violatility[row[0]] = volatility
            self.collector.put(dict(action=row[0], volatility=volatility))

def define_nul():
    for key, val in dict_violatility.items():
        if val == Decimal('0'):
            nul.append(key)
    for i in nul:
        del dict_violatility[i]
    nul.sort()



def collect_adress_files(folder):
    folders = []
    for i in os.walk(folder):
        folders.append(i)
    for address, dirs, files in folders:
            for file in files:
                file_adress.append(os.path.join(address, file))

def show(data):
    for i in range(3):
        keymax = max(data, key=data.get)
        print(f'{keymax} - {data[keymax]}')
        data.pop(keymax)

    # define_nul()

    for i in range(3):
        keymin = min(data, key=data.get)
        print(f'{keymin} - {data[keymin]}')
        data.pop(keymin)

    print('Null violatility:')
    print(','.join(nul))

@time_track
def main():
    collector = multiprocessing.Queue()
    ones = [Violatility(file=file, collector=collector) for file in file_adress]

    for one in ones:
        one.start()
    while not collector.empty():
        data = collector.get()
    for one in ones:
        one.join()

    print(data)

file_adress = []
folder = 'trades'
collect_adress_files(folder)

if __name__ == '__main__':
    main()