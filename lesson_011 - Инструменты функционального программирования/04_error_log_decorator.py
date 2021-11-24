# -*- coding: utf-8 -*-

# Написать декоратор, который будет логировать (записывать в лог файл)
# ошибки из декорируемой функции и выбрасывать их дальше.
#
# Имя файла лога - function_errors.log
# Формат лога: <имя функции> <параметры вызова> <тип ошибки> <текст ошибки>
# Лог файл открывать каждый раз при ошибке в режиме 'a'
import functools


# def log_errors(func):
#     @functools.wraps(func)
#     def surrogate(*args, **kwargs):
#         args_repr = [repr(a) for a in args]
#         kwargs_repr = [f'{k}={v!r}' for k, v in kwargs.items()]
#         signature = ','.join(args_repr + kwargs_repr)
#         try:
#             result = func(*args, **kwargs)
#         except Exception as exc:
#             print(f'В функции - {func.__name__} с параметрами {signature} ошибка {exc}')
#             with open('function_errors.log', 'a') as file:
#                 file.write(f'В функции - {func.__name__} с параметрами {signature} ошибка {exc}\n')
#
#         return result
#
#     return surrogate
def log_errors(log):
    def log_errors_1(func):
        @functools.wraps(func)
        def surrogate(*args, **kwargs):
            args_repr = [repr(a) for a in args]
            kwargs_repr = [f'{k}={v!r}' for k, v in kwargs.items()]
            signature = ','.join(args_repr + kwargs_repr)
            try:
                result = func(*args, **kwargs)
            except Exception as exc:
                print(f'В функции - {func.__name__} с параметрами {signature} ошибка {exc}')
                with open(log, 'a') as file:
                    file.write(f'В функции - {func.__name__} с параметрами {signature} ошибка {exc}\n')

            return result

        return surrogate
    return log_errors_1






# Проверить работу на следующих функциях
@log_errors('function_errors.log')
def perky(param):
    return param / 0


# perky(1)

@log_errors('function_errors.log')
def check_line(line):
    name, email, age = line.split(' ')
    if not name.isalpha():
        raise ValueError("it's not a name")
    if '@' not in email or '.' not in email:
        raise ValueError("it's not a email")
    if not 10 <= int(age) <= 99:
        raise ValueError('Age not in 10..99 range')


lines = [
    'Ярослав bxh@ya.ru 600',
    'Земфира tslzp@mail.ru 52',
    'Тролль nsocnzas.mail.ru 82',
    'Джигурда wqxq@gmail.com 29',
    'Земфира 86',
    'Равшан wmsuuzsxi@mail.ru 35',
]
for line in lines:
    try:
        check_line(line)
    except Exception as exc:
        print(f'Invalid format: {exc}')

perky(param=42)

# Усложненное задание (делать по желанию).
# Написать декоратор с параметром - именем файла
#
# @log_errors('function_errors.log')
# def func():
#     pass
