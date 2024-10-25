import os, time

directory = '.'
for root, dirs, files in os.walk(directory):
    for file in files:
        pass
        filepath = os.path.join(directory, file)
        filetime = os.path.getmtime(file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(file)
        parent_dir = os.path.dirname(filepath)

        print(f'Обнаружен файл {file}\n   '
              f'Путь: {filepath}.\n   '
              f'Размер: {filesize} байт, время изменения: {formatted_time}.\n   '
              f'Родительская директория: {parent_dir}')
