import os

for i in os.walk('.'):
    print (i)

print('Текущая директория:', os.getcwd())
print(os.getcwd())
# os.mkdir('Projekt7')

if os.path.exists('Projekt7'): #проверяет наличие папки в директории по указанному пути
    os.chdir('Projekt7')
else:
    os.mkdir('Projekt7')
    os.chdir('Projekt7')
print('Текущая директория:', os.getcwd())

# #созд. неск. вложенных папок
# os.makedirs('one/finger')
# os.makedirs(r'two\fut')
# os.mkdir('D:/Python/LESS - 03/LESS-08/')

print(os.listdir()) #список папок в текущем пространстве (без вложенности)
# для просмотра вложееных файлов исп. метод os.walk('.'), где '.' - текущ. директория
for i in os.walk('.'):
    print(i)

os.chdir(r'D:\Python\LESS - 03\LESS-07') #скопировали абсол. путь текущ. папки
print('Текущая директория:', os.getcwd())

# отсортируем файлы и папки по спискам
file = [f for f in os.listdir() if os.path.isfile(f)]
dirs = [d for d in os.listdir() if os.path.isdir(d)]
print(file)
print(dirs)

#запуск файлов и сбор о них информации
os.startfile(file[6])
print(os.stat(file[2])) #статистика о файле
print(os.stat(file[2]).st_size) #размер файла в байтах

# команды, выполняемые тж. в терминале
# os.system('pip install random2')
