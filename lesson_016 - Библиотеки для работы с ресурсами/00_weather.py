#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создать модуль-движок с классом WeatherMaker, необходимым для получения и формирования предсказаний.
# В нём должен быть метод, получающий прогноз с выбранного вами сайта (парсинг + re) за некоторый диапазон дат,
# а затем, получив данные, сформировать их в словарь {погода: Облачная, температура: 10, дата:datetime...}

# Добавить класс ImageMaker.
# Снабдить его методом рисования открытки
# (использовать OpenCV, в качестве заготовки брать lesson_016/python_snippets/external_data/probe.jpg):
#   С текстом, состоящим из полученных данных (пригодится cv2.putText)
#   С изображением, соответствующим типу погоды
# (хранятся в lesson_016/python_snippets/external_data/weather_img ,но можно нарисовать/добавить свои)
#   В качестве фона добавить градиент цвета, отражающего тип погоды
# Солнечно - от желтого к белому
# Дождь - от синего к белому
# Снег - от голубого к белому
# Облачно - от серого к белому

# Добавить класс DatabaseUpdater с методами:
#   Получающим данные из базы данных за указанный диапазон дат.
#   Сохраняющим прогнозы в базу данных (использовать peewee)

# Сделать программу с консольным интерфейсом, постаравшись все выполняемые действия вынести в отдельные функции.
# Среди действий, доступных пользователю должны быть:
#   Добавление прогнозов за диапазон дат в базу данных
#   Получение прогнозов за диапазон дат из базы
#   Создание открыток из полученных прогнозов
#   Выведение полученных прогнозов на консоль
# При старте консольная утилита должна загружать прогнозы за прошедшую неделю.

# Рекомендации:
# Можно создать отдельный модуль для инициализирования базы данных.
# Как далее использовать эту базу данных в движке:
# Передавать DatabaseUpdater url-путь
# https://peewee.readthedocs.io/en/latest/peewee/playhouse.html#db-url
# Приконнектится по полученному url-пути к базе данных
# Инициализировать её через DatabaseProxy()
# https://peewee.readthedocs.io/en/latest/peewee/database.html#dynamically-defining-a-database
import random
import re
from datetime import datetime, date
from pprint import pprint
import os
import cv2
import requests
import bs4
import peewee

class WeatherMaker(object):
    def __init__(self):
        self.SITE = 'https://www.gismeteo.ru/weather-moscow-4368/month/'

        self.MONTH = {'янв': 1,
             'фев': 2,
             'мар': 3,
             'апр': 4,
             'май': 5,
             'июн': 6,
             'июл': 7,
             'авг': 8,
             'сен': 9,
             'окт': 10,
             'ноя': 11,
             'дек': 12}

        self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; '
                             'Linux x86_64; rv:94.0) Gecko/20100101 '
                             'Firefox/94.0'}

        self.re_data = r'\d+\s\w+'
        self.re_day = r'\d+'
        self.re_month = r'\D+'

    def parsing(self):
        self.html = requests.get(self.SITE, headers=self.headers)
        self.soup = bs4.BeautifulSoup(self.html.content, 'html.parser')
        self.items = self.soup.findAll('div', class_=lambda value: value and value.startswith('tooltip cell'))
        if not self.items:
            self.items = self.soup.findAll('a', class_=lambda value: value and value.startswith('row'))
        self.weather = self.soup.findAll('div', class_='tooltip cell _hover')
        return self.items

    def receive_weather(self):
        # dict_weather = {}
        list_weather = []
        print('what a fuck')
        for i in self.items:
            number_day = i.find('div', class_='date').string.strip()
            if number_day is None:
                number_day = i.find('div', class_=lambda value: value and value.startswith('date')).string.strip()
            temp_day = i.find('span', class_='value unit unit_temperature_c')
            if temp_day is None:
                temp_day = i.find('span', class_='unit unit_temperature_c')
            try:
                temp = temp_day.string.strip()
            except AttributeError:
                temp = None
            try:
                weather = i.attrs['data-text']
            except KeyError:
                weather = random.choice(['Снег', 'Дождь', 'Облачно', 'Солнечно'])
                # weather = None #ставим костыли т.к. гисметео поменяло свой сайт, и теперь погода отображается
                # только сложной картинкой
            if re.match(self.re_data, number_day):
                year = int(datetime.now().year)
                month_for_dict = re.search(self.re_month, number_day)[0].strip()
                number_month = self.MONTH[month_for_dict]
                day = int(re.search(self.re_day, number_day)[0].strip())
                date = datetime(year=year, month=number_month, day=day, )
                # dict_weather[date] = {'temp': temp, 'weather': weather}
                list_weather.append({'date': date, 'temp': temp, 'weather': weather})
                month = re.search(self.re_month, number_day).group(0)
            else:
                number_day += month
            year = int(datetime.now().year)
            month_for_dict = re.search(self.re_month, number_day)[0].strip()
            number_month = self.MONTH[month_for_dict]
            day = int(re.search(self.re_day, number_day)[0].strip())
            if number_month == 1 and int(datetime.now().month == 12):
                year += 1
            date = datetime(year=year, month=number_month, day=day,)
            # dict_weather[date] = {'temp': temp, 'weather': weather}
            print(number_day is None)
            list_weather.append({'date': date, 'temp': temp, 'weather': weather})
        return list_weather

class ImageMaker(object, ):
    def __init__(self, dict_weather):
        self.image = cv2.imread('python_snippets/external_data/probe.jpg')
        self.snow = cv2.imread('python_snippets/external_data/snow.jpg')
        self.cloud = cv2.imread('python_snippets/external_data/obl.png')
        self.rain = cv2.imread('python_snippets/external_data/rain.png')
        self.sunny = cv2.imread('python_snippets/external_data/sunny.jpeg')
        self.dict_weather = dict_weather
        self.COLOR = {'grey': (120, 120, 120),
                      'dark_blue': (255, 0, 0),
                      'yellow': (0, 255, 255),
                      'blue': (255, 255, 0),}

    def run(self):
        for key in self.dict_weather.keys():
            dict = self.dict_weather[key]
            self.define_param_img(dict)
            self.grad_color()
            self.input_image()
            self.write_on_image(key)
            self.viewImage()

    def define_param_img(self, dict):
        dict = dict
        weather = dict['weather'].lower()
        snow = r'снег'
        rain = r'дожд'
        cloud = r'обл|пасм'
        sunny = r'солн'
        self.temp = dict['temp']
        if re.search(snow, weather):
            self.color = self.COLOR['blue']
            self.icon = self.snow
        elif re.search(rain, weather):
            self.color = self.COLOR['dark_blue']
            self.icon = self.rain
        elif re.search(cloud, weather):
            self.color = self.COLOR['grey']
            self.icon = self.cloud
        elif re.search(sunny, weather):
            self.color = self.COLOR['yellow']
            self.icon = self.sunny
        else:
            self.color = None
            self.icon = None
        return self.color, self.icon

    def grad_color(self):
        self.image_with_grad = self.image.copy()
        x_0 = y_0 = x_1 = 0
        y_1 = self.image_with_grad.shape[0]
        b, g, r = self.color
        delta = self.image_with_grad.shape[1] // (255 - 120)
        if delta < 1:
            delta = 1
        for i in range(255):
            if r > 255: r = 255
            if b > 255: b = 255
            if g > 255: g = 255
            cv2.line(self.image_with_grad, (x_0, y_0), (x_1, y_1), (b, g, r), delta)
            x_0 += delta
            x_1 += delta
            r += 1
            b += 1
            g += 1
        return self.image_with_grad

    def viewImage(self):
        cv2.namedWindow('card', cv2.WINDOW_NORMAL)
        cv2.imshow('card', self.image_with_grad)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    #создадим функцию вставки картинки
    def input_image(self):
        required_size_x = 128
        available_size_x = self.icon.shape[1]
        scale_percent = required_size_x / available_size_x * 100  # Процент от изначального размера
        width = int(self.icon.shape[1] * scale_percent / 100)
        height = int(self.icon.shape[0] * scale_percent / 100)
        dim = (width, height)
        new_image = cv2.resize(self.icon, dim, interpolation=cv2.INTER_AREA)
        x_offset = 20
        y_offset = self.image_with_grad.shape[0] // 4
        self.image_with_grad[y_offset: y_offset+new_image.shape[0], x_offset: x_offset+new_image.shape[1]] = new_image
        return self.image_with_grad

    #Напишем на рисунке
    def write_on_image(self, date):
        font = 1
        fontscale = 2
        color_letter = (0, 0, 0)
        org = (250, 50)
        cv2.putText(img=self.image_with_grad, text='Moscow', org=org, fontFace=font, fontScale=fontscale, color=color_letter)
        text = f'{date: %d.%m.%Y }'
        org_date = (200, 80)
        cv2.putText(img=self.image_with_grad, text=text, org=org_date, fontFace=font, fontScale=fontscale, color=color_letter)
        text_temp = self.temp
        # text_temp = self.temp.encode(encoding='utf-8').decode(encoding='ASCII', errors='ignore')
        org_temp = (260, 110)
        cv2.putText(img=self.image_with_grad, text=text_temp, org=org_temp, fontFace=font, fontScale=fontscale,
                    color=color_letter)
        return self.image_with_grad

database = peewee.SqliteDatabase('weather.db')

class DatabaseUpdater(object):
    def __init__(self, weather_for_db):
        self.weather_for_db = weather_for_db

    def save_weather(self, ):
        # Создание таблиц:
        database.create_tables([Weather])
        Weather.insert_many(self.weather_for_db).execute()

    def take_weather(self, date_1, date_2=None):
        dict = {}
        if date_2 == None:
            dat = Weather.get(Weather.date == date_1)
            dict[dat.date] = {'temp': dat.temp, 'weather': dat.weather}
        else:
            for dat in Weather.select().where((Weather.date >= date_1) & (Weather.date <= date_2)):
                dict[dat.date] = {'temp': dat.temp, 'weather': dat.weather}
        return dict

class BaseTable(peewee.Model):
    # В подклассе Meta указываем подключение к той или иной базе данных
    class Meta:
        database = database


# Чтобы создать таблицу в нашей БД, нам нужно создать класс
class Weather(BaseTable):
    date = peewee.DateTimeField()
    temp = peewee.CharField()
    weather = peewee.CharField()





a = WeatherMaker()
a.parsing()
print(a)
b = a.receive_weather()
print('parsing', b)
c = DatabaseUpdater(b)
c.save_weather()
while True:
    print('Ввберите действие:\n'
            '1 - Получить прогнозы за диапазон дат(если интересует одна дата - вторую оставь пустой)\n'
            '2 - Создать открытки из полученных прогнозов\n'
            '3 - Выйти из программы')
    action = input(': ').strip()
    if action == '3':
        try:
            os.remove('weather.db')
        except BaseException:
            print('Вы и не создавали базу')
        break
    elif action == '1':
        year_1 = int(input('year: ').strip())
        number_month_1 = int(input('number_month: ').strip())
        day_1 = int(input('day: ').strip())
        date_1 = datetime(year=year_1, month=number_month_1, day=day_1, )
        print('введи вторую дату, если требуется диапазон')
        try:
            year_2 = int(input('year: ').strip())
            print('год введен')
        except BaseException:
            year_2 = None
        if year_2:
            number_month_2 = int(input('number_month: ').strip())
            day_2 = int(input('day: ').strip())
            date_2 = datetime(year=year_2, month=number_month_2, day=day_2, )
        else:
            date_2 = None
        # print(date_1, date_2)
        dict = c.take_weather(date_1, date_2)
        pprint(dict)
    elif action == '2':
        if dict:
            card = ImageMaker(c.take_weather(date_1, date_2))
            card.run()
        else:
            print('Не выбран диапозон дат')
    else:
        print('<Unknown command>')
#необходимы следующие доработки в программу:
#1 - разобраться с кодировкой в CV минус в виде знаков вопроса не канает
#2 - сделать проверку на валидность номера месяца и дня, если не верно - предложить другое
#3 - если в БД даты отсутствуют - сообщить об этом и запросить другие.
#4 - если диапазон "отрицателен" менять дату 1 и дату 2
#
