#/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


def check_reg(line):
    if len(line.split()) != 3:
        raise ValueError('Не все поля заполнены')
    else:
        name, email, age = line.split(' ')
        if not name.isalpha():
            raise NotNameError('Некорректное имя')
        elif not ('@' in email and '.' in email):
            raise NotNameError('Некореектный мейл')
        elif not (int(age) in range(10, 100)):
            raise ValueError('Возраст указан неверно')

i = 1
with open('registrations.txt', 'r') as ff:
    for line in ff:
        try:
            check_reg(line)
            with open('registrations_good.log', 'a') as file:
                file.write(f'{line} ')
        except Exception as exc:
            with open('registrations_bad.log', 'a') as file:
                file.write(f'строка {i} содержание {line[:-1]} событие {exc} \n')
        finally:
            i += 1