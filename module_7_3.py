class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    words = file.read().split().lower()
                    words_dict[file_name] = words
            except FileNotFoundError:
                print(f'Файл {file_name} не найден.')
            except Exception as e:
                print(f"Ошибка при чтении файла {file_name}: {e}")
        return all_words

    def find(self, word):
        result = {}
        all_words = self.get_all_words()  # Получаем все слова

        for file_name, words in all_words.items():
            if word in words:
                result[file_name] = words.index(word)
            return result

    def count(self, word):
        result = {}
        all_words = self.get_all_words()  # Получаем все слова

        for file_name, words in all_words.items():
            count = words.count(word)  # Считаем количество вхождений
            if count > 0:
                result[file_name] = count  # Добавляем только если больше 0

        return result

    def __repr__(self):
        return f'WordsFinder(file_names = {self.file_names})'


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
