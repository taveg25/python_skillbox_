#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел
import time


def get_time_track(precision):
    def time_track(func):
        # практически тот же самый time_track, за исключением точности вывода времени
        def surrogate(*args, **kwargs):
            started_at = time.time()
            result = func(*args, **kwargs)
            ended_at = time.time()
            elapsed = round(ended_at - started_at, precision)  # отличия в этой строке
            print(f'Функция работала {elapsed} секунд(ы)')
            return result
        return surrogate
    return time_track


# def get_prime_numbers(n):
#     prime_numbers = []
#     for number in range(2, n+1):
#         for prime in prime_numbers:
#             if number % prime == 0:
#                 break
#         else:
#             prime_numbers.append(number)
#     return prime_numbers
#
# @get_time_track(precision=6)
# def print_with_block(n):
#         for number in get_prime_numbers(n=n):
#             print(number)
#
# print_with_block(10000)
# # Часть 1
# # На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# # который выдает последовательность простых чисел до n
# #
# # Распечатать все простые числа до 10000 в столбик
#
#
# class PrimeNumbers(object):
#     """" Итератор последовательности простых чисел до n"""
#
#     def __init__(self, n):
#         self.i = 2
#         self.prime_numbers = [2]
#         self.n = n
#
#     def __iter__(self):
#         self.i = 1
#         self.prime_numbers = []
#         return self
#
#     def __next__(self):
#         self.i += 1
#         if self.i > 1:
#             if self.i > self.n:
#                 raise StopIteration()
#             if 0 not in (map((lambda x: self.i % x), self.prime_numbers)):
#                 self.prime_numbers.append(self.i)
#                 return self.i
#             else:
#                 return self.__next__()
#
# @get_time_track(precision=6)
# def print_with_iterator(n):
#     prime_number_iterator = PrimeNumbers(n=n)
#     for number in prime_number_iterator:
#         print(number)
#
# print_with_iterator(10000)
#
# # Часть 2
# # Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# # Распечатать все простые числа до 10000 в столбик
#
#
def prime_numbers_generator(n):
    prime_numbers = []
    for number in range(2, n+1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
            yield number

@get_time_track(precision=6)
def print_with_generator(n):
    for number in prime_numbers_generator(n=n):
        print(number)

print_with_generator(10000)
# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.
