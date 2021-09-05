#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for


sd.resolution = (1200, 600)
for y in range(-20, 801, 50):
    for x in range(-50, 1201, 100):
        if y%20 == 0:
            x += 50
        left_botton = sd.get_point(x, y)
        right_botton = sd.get_point(x + 100, y + 50)
        sd.rectangle(left_botton, right_botton, width=1)


sd.pause()
