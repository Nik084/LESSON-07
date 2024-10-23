class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = []
        for i in file_names:
            self.file_names.append(i)
        # print(self.file_names)

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with (open (i, encoding='utf-8') as file):
                file_cont = file.read().lower()
                while '\n\n' in file_cont:
                    file_cont = file_cont.replace('\n\n', '\n')
                del_simbols = [',', '.', '=', '!', '?', ';', ':', ' - ']
                for l in del_simbols:
                    file_cont = file_cont.replace(l+'\n', ' ').replace(l, '')
                file_cont = file_cont.replace('\n', ' ')
                all_words[i] = file_cont.strip().split(' ')
                # print(file_cont)
        return all_words

    def find(self, word):
        self.word = word.lower()
        numb_find = {}
        for name, words in self.get_all_words().items():
            for k in range(len(words)):
                if words[k] == self.word:
                    numb_find[name] = k+1
                    break
                else:
                    numb_find[name] = '(!) Искомое слово не найдено'
        return numb_find

    def count(self, word):
        self.word = word.lower()
        result = {}
        for name, words in self.get_all_words().items():
            result[name] = 0 #len(words)
            for k in words:
                if k == self.word: # !=
                    result[name] += 1 #-= 1
        return result

finder2 = WordsFinder('list.txt', 'nota.txt', 'nota2.txt')
print(finder2.get_all_words()) # Все слова
print(f'Значение первого упоминания слова в тексте:\n{finder2.find('of')}')
print(f'Искомых слов в тексте всего:\n{finder2.count('of')}')