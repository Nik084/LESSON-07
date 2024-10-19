info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
file_name = 'nota.txt'

def custom_write(file_name, strings):
    dict_ = {}
    for i in range (len(strings)):
        file = open(file_name, 'a', encoding='utf-8')
        dict_[(i+1, file.tell())] = strings[i]
        file.write(f'{strings[i]}\n')
        file.close()
    return dict_

result = custom_write('nota.txt', info)
for dict_ in result.items():
  print(dict_)
