#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ").strip()
month = int(user_input)
print('Вы ввели', month)
#мне не нравится идея делать все через элифы 10 раз, по-моему это туповато, поэтому словарь и даже перевод строки в инт тут не шибко то нужен,


dict_days_in_month={'1':'31 день', '2':'28 дней', '3':'31 день',
                    '4':'30 дней', '5':'31 день', '6':'30 дней',
                    '7':'31 день', '8':'31 день', '9':'30 дней',
                    '10':'31 день', '11':'30 дней', '12':'31 день'}
#print(list(dict_days_in_month.keys()))
if user_input in list(dict_days_in_month.keys()):
    print('В указанном месяце', dict_days_in_month[user_input])
else:
    print('Номер месяца введен некорректно')