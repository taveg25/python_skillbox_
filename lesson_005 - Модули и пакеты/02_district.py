#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from district.central_street.house1 import room1 as cs_h1_r1, room2 as cs_h1_r2
from district.central_street.house2 import room1 as cs_h2_r1, room2 as cs_h2_r2
from district.soviet_street.house1 import room1 as ss_h1_r1, room2 as ss_h1_r2
from district.soviet_street.house2 import room1 as ss_h2_r1,room2 as ss_h2_r2

list_falks_cs = []
list_falks_ss = []
list_falks_cs.extend(cs_h1_r1.folks)
list_falks_cs.extend(cs_h1_r2.folks)
list_falks_cs.extend(cs_h2_r1.folks)
list_falks_cs.extend(cs_h2_r2.folks)

list_falks_ss.extend(ss_h1_r1.folks)
list_falks_ss.extend(ss_h1_r2.folks)
list_falks_ss.extend(ss_h2_r1.folks)
list_falks_ss.extend(ss_h2_r2.folks)

print('В центральном районе живут:', ', '.join(list_falks_cs))
print('В советстком районе живут:', ', '.join(list_falks_ss))
