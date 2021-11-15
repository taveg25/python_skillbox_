# -*- coding: utf-8 -*-

import csv
import json
import re
from collections import defaultdict
from datetime import datetime
from decimal import Decimal, ROUND_HALF_EVEN
from pprint import pprint
#
# # mob = 'Mob_exp201_tm200.0'
# # re_exp = r'Mob_exp(\d*)_.*'
# # re_tm = r'.*_tm(\d*.*)'
# # loc = 'Location_12_tm0.0987654320'
# # exp = int(re.search(re_exp, mob)[1])
# # time = Decimal(re.search(re_tm, loc)[1])
# #
# # print(type(mob) == str)
#
# with open("rpg.json", "r") as read_file:
#     data = json.load(read_file)
# data_path = "data['Location_0_tm0']"
# # c += '[1]'
# # c += '[2]'
# # c += "['Location_1_tm10400000']"
# # [2]['Location_3_tm330000000'][0]['Location_7_tm333000000'][0]"
#
#
#
# d = eval(data_path)
#
# for x in (d):
#     if type(x) == str:
#         print(x)
#     elif type(x) == dict:
#         for key in x.keys():
#             print(key)
#     elif type(x) == list:
#         for t in x: print(t)
# print(type(d))
#
# if type(d) == list:
#     locs = []
#     locs2 = []
#     for i in d:
#         if type(i) == dict:
#             for key in i.keys():
#                 locs.append(key)
#                 locs2.append(i)
#     print('What directory?')
#     for j in range(len(locs)):
#         print(f'{j + 1} - {locs[j]}')
#         print(data_path + '[' + str(d.index(locs2[j])) + '][' + locs[j] + ']')

import datetime
# print(str(datetime.timedelta(seconds=123456789.0987654321)))
time_start = datetime.datetime.now()
a = 34**456799
seconds = (datetime.datetime.now() - time_start)
print('{%H:%M:%S}'.format(seconds))