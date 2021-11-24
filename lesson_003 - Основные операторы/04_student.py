#!/bin/usr/env python3
# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей
#мне показалось, что интереснее все-таки посчитать разные случаи денежного довольствия, таким
# образом и усовершенствовал решение
educational_grant, expenses = 15000, 12000


month = 1
prihod = educational_grant
rashod_in_month = expenses
rashod_all = rashod_in_month
while month < 10:
    month +=1
    rashod_in_month = rashod_in_month * 1.03
    rashod_all +=rashod_in_month
    prihod += educational_grant
    delta = round(prihod - rashod_all, 2)
if delta < 0:
    delta = delta * (-1)
    print ('Студенту необходимо попросить', delta, 'рублей')
else:
    print('Студенту хватает денег. Останется', delta, 'рублей')