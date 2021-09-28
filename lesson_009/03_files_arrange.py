# -*- coding: utf-8 -*-

import os, time, shutil

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk - получение кортежей для каждого каталога в папке
#   os.path.dirname - получение имени каталога в пути патх
#   os.path.join - соединение компонентов путей файловой системы
#   os.path.normpath - нормализация имени пути
#   os.path.getmtime - время в секундах с начала эпохи
#   time.gmtime - время из времени с начала эпохи преобразует в нормальное
#   os.makedirs - создание каталога любого уровня
#   shutil.copy2 - копирует данные с сохранением метаданных
# os.path.exists(path) - True, если указан существующий путь
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
import zipfile


class SpreaderFiles(object):

    def __init__(self, in_folder, out_folder):
        self.in_folder = in_folder
        self.out_folder = out_folder
        self.folder = []
        self.file_adress = []


    def collect_adress_files(self):
        for i in os.walk(self.in_folder):
            self.folder.append(i)
        for adress, dirs, files in self.folder:
             for file in files:
                 self.file_adress.append(os.path.join(adress, file))

    def get_copy(self):
        for file in self.file_adress:
            path = os.path.join(os.getcwd(), self.out_folder,
                                str(time.gmtime(os.path.getmtime(file))[0]), str(time.gmtime(os.path.getmtime(file))[1]))
            if os.path.exists(path):
                shutil.copy2(file, path)
            else:
                os.makedirs(path)
                shutil.copy2(file, path)


class SpreaderFilesZip(SpreaderFiles):

    def __init__(self, zip_folder, out_folder):
        super().__init__(in_folder=zipfile.ZipFile(zip_folder, 'r'), out_folder=out_folder)

    def collect_adress_files(self):
        pass

    def get_copy(self):
        for file_info in self.in_folder.infolist():
            if file_info.file_size > 0:
                path = os.path.join(os.getcwd(), self.out_folder,
                                    str(file_info.date_time[0]), str(file_info.date_time[1]))
                if os.path.exists(path):
                    self.in_folder.extract(file_info.filename, path=path)
                else:
                    os.makedirs(path)
                    self.in_folder.extract(file_info.filename, path=path)






inf = SpreaderFilesZip('icons.zip', 'icon_by_ear_4')
inf.collect_adress_files()
inf.get_copy()






# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828


