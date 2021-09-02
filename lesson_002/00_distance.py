#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pprint import pprint
# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}
x_moscow=sites['Moscow'][0]
y_moscow=sites['Moscow'][1]

x_london=sites['London'][0]
y_london=sites['London'][1]

x_paris=sites['Paris'][0]
y_paris=sites['Paris'][1]

moscow_london=((x_moscow-x_london)**2+(y_moscow-y_london)**2)**.5
moscow_paris=((x_moscow-x_paris)**2+(y_moscow-y_paris)**2)**.5
london_paris=((x_london-x_paris)**2+(y_london-y_paris)**2)**.5
# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = {}
distances['Moscow']={}
distances['Moscow']['London']=moscow_london
distances['Moscow']['Paris']=moscow_paris
distances['London']={}
distances['London']['Moscow']=moscow_london
distances['London']['Paris']=london_paris
distances['Paris']={}
distances['Paris']['Moscow']=moscow_paris
distances['Paris']['London']=london_paris


pprint(distances)




