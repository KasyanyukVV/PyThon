print("№1-----------------------------")
print("Привет")      # " " или ' ' - текст
print(type("Привет"))    # `str` или `string - текст (тип данных)
print("4" + "4")

print('№2-----------------------------')
print(6)
print(type(6))    # int или integer - целое число (тип данных)
print(6 / 2)    # // - целочисленное деление, / - деление
print(type(3.0))    # float - число с плавуюшей точкой (тип данных)

print('№3-----------------------------')
print(type(True), type(False))    # bool или boolean - логический (тип данных)
print(5 < 2, 5 > 2, 10 <= 10, 10 >= 15, 10 == 15, 10 != 15)
print(5 != 5 and 5 < 10, 5 == 5 and 5 < 10)  # and - и ; or - или

print('№4-----------------------------')
print(type(int('5')))     # перевод из текстового типа данных в числовой тип данных
print(type(str(5)))      # перевод из числового типа данных в текстовый тип данных

print('№5 Как проверить то, что каждое слово в строке начинается с заглавной буквы?')
# istitle() проверяет, начинается ли каждое слово в строке с заглавной буквы.
print('The Hilton'.istitle())        # => True
print('The dog'.istitle())           # => False
print('sticky rice'.istitle())       # => False

print('№6 Как найти индекс первого вхождения подстроки в строку?')
# Метод find() возвращает -1 в том случае, если искомая подстрока в строке не найдена.
print('The worlds fastest plane'.find('plane'))        # => 19
print('The worlds fastest plane'.find('car'))          # => -1
# Метод index() в подобной ситуации выбрасывает ошибку ValueError
print('The worlds fastest plane'.index('plane'))       # => 19
print('The worlds fastest plane'.index('car'))