import os
import time

directory = r"D:\pythonProjectsForUniversity\pythonProject\module_7_5_dz" # копируем полный путь до директории
for root, dirs, files in os.walk(directory): # (корень(пути) дериктории,список директорий, файл)
    for file in files:
        filepath = os.path.join(root,file) #после join идент подсказка (path, paths)- пути и файл
        filetime =  os.path.getmtime(filepath) # нужен filename - это falepath
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath) # нужен filename - это falepath
        parent_dir = os.path.dirname(filepath) # нужен filename - это falepath
        print( f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт,'
            f' Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
        directory = "."
