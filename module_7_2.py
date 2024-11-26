
def custom_write(file_name, strings):
    strings_positions = {}

    with open(file_name, 'w', encoding='utf-8') as file:
        for i, line in enumerate(strings, start=1):
            position = file.tell()                          # Получаем текущую позицию в байтах
            file.write(line + '\n')                         # Записываем строку в файл с новой строки
            strings_positions[(i, position)] = line         # Сохраняем информацию в словарь

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



