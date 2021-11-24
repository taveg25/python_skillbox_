#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013 - Стандартные и сторонние библиотеки питон/images/ticket_template.png
# Пример заполнения lesson_013 - Стандартные и сторонние библиотеки питон/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru
import os
from PIL import Image, ImageDraw, ImageFont, ImageColor


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


make_ticket('Терещенко Е.Ю.', 'Москва', 'Иркутск', '24.10', )
# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля agrparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.
