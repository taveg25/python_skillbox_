#!/usr/bin/env: python3
# -*- coding: utf-8 -*-

# стена, крыша, окно - дом
# смайлик
import simple_draw as sd

def wall(x, y):
    for y_1 in range(y, y+251, 25):
        for x_1 in range(x, x+401, 50):
            if (y_1 - y) % 10 == 0:
                x_1 += 25
            left_botton = sd.get_point(x_1, y_1)
            right_botton = sd.get_point(x_1 + 50, y_1 + 25)
            sd.rectangle(left_botton, right_botton, width=1)
    left_botton_external = sd.get_point(x, y)
    right_botton_external = sd.get_point(x + 475, y + 275)
    sd.rectangle(left_botton_external, right_botton_external, width=1)

def roof(x, y):
    point_1 = sd.get_point(x, y)
    point_2 = sd.get_point(x+500, y)
    point_3 = sd.get_point(x+250, y+200)
    point_list = [point_1, point_2, point_3]
    sd.polygon(point_list, color=sd.COLOR_DARK_RED, width=0)

def window(x, y):
    point_1_window_frame = sd.get_point(x, y)
    point_2_window_frame = sd.get_point(x + 120, y + 175)
    sd.rectangle(point_1_window_frame, point_2_window_frame, color=sd.COLOR_WHITE, width=5)
    point_1_glass = sd.get_point(x + 3, y + 3)
    point_2_glass = sd.get_point(x + 117, y + 172)
    sd.rectangle(point_1_glass, point_2_glass, color=sd.COLOR_BLUE, width=0)

def smile(x, y):
    x_centr = x
    y_centr = y
    radius = 50
    centr_position = sd.get_point(x_centr, y_centr)
    sd.circle(centr_position, radius, width=0)
    right_eye_position = sd.get_point(x_centr + 25, y_centr + 20)
    left_eye_position = sd.get_point(x_centr - 25, y_centr + 20)
    right_month_position = sd.get_point(x_centr + 15, y_centr - 20)
    left_month_position = sd.get_point(x_centr - 15, y_centr - 20)
    sd.circle(left_eye_position, 10, sd.COLOR_BLACK, width=0)
    sd.circle(right_eye_position, 10, sd.COLOR_BLACK, width=0)
    sd.line(right_month_position, left_month_position, sd.COLOR_BLACK, width=10)

def house(x, y):
    wall(x, y)
    window(x + 150, y + 50)
    smile(x + 210, y + 150)
    roof(x - 10, y + 276)



