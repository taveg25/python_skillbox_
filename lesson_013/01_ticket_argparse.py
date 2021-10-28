#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru
import os
import argparse
from PIL import Image, ImageDraw, ImageFont, ImageColor

parser = argparse.ArgumentParser()
parser.add_argument('fio', help='fio is fio of passenger')
parser.add_argument('from_', help='from what city passenger is flying')
parser.add_argument('to', help='to what city passenger is flying')
parser.add_argument('date', help='from what date passenger is flying')
parser.add_argument('--out_path', help='file to save ticket')
args = parser.parse_args()


def make_ticket(fio, from_, to, date=None, out_path=None):
    im = Image.open('images/ticket_template.png')
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(os.path.join('fonts', 'Mononoki.ttf'), size=22)
    font2 = ImageFont.truetype(os.path.join('fonts', 'Mononoki.ttf'), size=18)
    message_fio = f'{fio}'
    draw.text((45, 120), message_fio, font=font, fill=ImageColor.colormap['black'])
    message_from = f'{from_}'
    draw.text((45, 185), message_from, font=font, fill=ImageColor.colormap['black'])
    message_to = f'{to}'
    draw.text((45, 252), message_to, font=font, fill=ImageColor.colormap['black'])
    message_date = f'{date}'
    draw.text((280, 255), message_date, font=font2, fill=ImageColor.colormap['black'])

    im.show()
    if out_path:
        im.save(out_path)


make_ticket(args.fio, args.from_, args.to, args.date, args.out_path )
# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля agrparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.
