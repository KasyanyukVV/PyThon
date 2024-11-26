def custom_write(file_name, strings):
    strings_positions = {}

    # Открываем файл для записи с кодировкой utf-8
    file = open(file_name, 'w', encoding='utf-8')

    try:
        for index, string in enumerate(strings, start=1):
            byte_position = file.tell()  # Получаем текущую позицию в байтах
            file.write(string + '\n')  # Записываем строку в файл с новой строки
            strings_positions[(index, byte_position)] = string  # Сохраняем информацию в словарь
    finally:
        file.close()  # Закрываем файл

    return strings_positions

# Пример использования
if __name__ == "__main__":
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]
    result = custom_write('test.txt', info)

    for elem in result.items():
        print(elem)



