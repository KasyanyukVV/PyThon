# Это класс WordsFinder
class WordsFinder:
    # Метод для инициализации объекта
    def __init__(self, *file_txt):
        # Здесь сохраняем имена файлов
        self.file_names = file_txt

    # Метод для получения всех слов из файлов
    def get_all_words(self):
        # Словарь для хранения слов из файлов
        all_words = {}
        # Перебираем все файлы
        for i in self.file_names:
            # Пытаемся открыть файл
            with open(i, 'r', encoding='utf-8') as file:
                # Читаем текст из файла и сразу делаем его маленькими буквами
                text = file.read()
                text = text.lower()
                # Убираем разные знаки препинания
                for j in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    text = text.replace(j, '')
                # Разбиваем текст на слова
                words = text.split()
                # Записываем слова в словарь
                all_words[i] = words
        # Возвращаем словарь
        return all_words

    # Метод для поиска слова в файлах
    def find(self, word):
        # Словарь для результата
        result = {}
        # Получаем все слова из файлов
        all_words = self.get_all_words()
        # Перебираем файлы и их слова
        for file_name, words in all_words.items():
            # Перебираем слова с номерами
            for i, w in enumerate(words):
                # Если слово совпало
                if w == word.lower():
                    # Запоминаем номер слова (нумерация с 1)
                    result[file_name] = i + 1
                    # Прекращаем поиск, так как нужно только первое вхождение
                    break
        # Возвращаем результат
        return result

    # Метод для подсчёта количества слов в файлах
    def count(self, word):
        # Словарь для результата
        result = {}
        # Получаем все слова из файлов
        all_words = self.get_all_words()
        # Перебираем файлы и их слова
        for file_name, words in all_words.items():
            # Считаем количество слова
            count = words.count(word.lower())
            # Сохраняем результат
            result[file_name] = count
        # Возвращаем результат
        return result


# Пример использования
finder = WordsFinder('test_file.txt')  # Создаём объект с файлом
print(finder.get_all_words())  # Показываем все слова
print(finder.find('TEXT'))  # Ищем слово "TEXT"
print(finder.count('teXT'))  # Считаем слово "teXT"
