#!/bin/usr/env python3
# -*- coding: utf-8 -*-

# В данном пакете разместим то, что создано природой - радугу, дерево, солнце, снег

import simple_draw as sd
import random as rd

x_centr = 600
y_centr = -300
radius = 500

def rainbow(x, y, rad):
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
    for i in range(7):
        centr_position = sd.get_point(x, y)
        color = rainbow_colors[i]
        sd.circle(centr_position, rad, color, width=9)
        rad += 9

def tree(point, angle, length):
    if length < 8:
        return 1
    color = sd.COLOR_YELLOW
    if length < 20:
        color = sd.COLOR_GREEN
    alpha = 20
    v_1 = sd.get_vector(start_point=point, angle=angle-alpha, length=length, width=1)
    v_2 = sd.get_vector(start_point=point, angle=angle+alpha, length=length, width=1)
    v_1.draw(color = color)
    v_2.draw(color = color)
    next_point_v_1 = v_1.end_point
    next_point_v_2 =v_2.end_point
    next_angle_v_1 = v_1.angle
    next_angle_v_2 = v_2.angle
    next_length = length * .75
    tree(point=next_point_v_1, angle=next_angle_v_1, length=next_length)
    tree(point=next_point_v_2, angle=next_angle_v_2, length=next_length)

def tree_draw(x,y, length):
    start_point = sd.get_point(x,y)
    end_point = sd.get_point(x, y + length)
    sd.line(start_point, end_point)
    point_1 = sd.get_point(x, y + length)
    tree(point_1, 90, length)


def snowflake(x,y):
    x_many, y_many = [], []
    length_rd = []
    for i in range(50):
        x_many.append(sd.random_number(x-100, x+100))
        y_many.append(sd.random_number(y-5, y+80))
        length_rd.append(sd.random_number(10, 30))
        point = sd.get_point(x_many[i], y_many[i])
        length = length_rd[i]
        sd.snowflake(center=point, length=length)

def sun(x, y):
    point = sd.get_point(x, y)
    sd.circle(point, 40, width=0)
    angle = 0
    for i in range(10):
        angle += 360/10
        v_1 = sd.get_vector(start_point=point, angle=angle, length=70, width=8)
        v_1.draw()

def land ():
    point_1_land = sd.get_point(0, 0)
    point_2_land = sd.get_point(1600, 50)
    sd.rectangle(point_1_land, point_2_land, color=sd.COLOR_DARK_ORANGE, width=0)
