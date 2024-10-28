# -*- coding: utf-8 -*-


class WordsFinder:
    def __init__(self, *file_names) -> None:
        self.file_names  = list(file_names)

    def get_all_words(self):  #return {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                file_string = file.read().lower()
                for punctuation in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        file_string = file_string.replace(punctuation, '')
                list_file_words = file_string.split()
                all_words[file_name] = list_file_words
        return all_words

    def find(self, word):
        word = word.lower()
        result = {}
        for file_name, words in self.get_all_words().items():
            if word in words:
                result[file_name] = words.index(word) + 1
        return result

    def count(self, word):
        word = word.lower()
        result = {}
        for file_name, words in self.get_all_words().items():
            result[file_name] = words.count(word)
        return result


if __name__ == '__main__':
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words()) # Все слова
    print(finder2.find('TEXT')) # 3 слово по счёту
    print(finder2.count('teXT')) # 4 слова teXT в тексте всего

    # Вывод на консоль:
    '''
    {'test_file.txt': ["it's", 'a', 'text', 'for', 'task', 'найти', 'везде', 'используйте', 'его', 'для', 'самопроверки', 'успехов', 'в', 'решении', 'задачи', 'text', 'text', 'text']}
    {'test_file.txt': 3}
    {'test_file.txt': 4}
    '''