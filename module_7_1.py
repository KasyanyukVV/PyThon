class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                return file.read().strip()
        except FileNotFoundError:
            return ""

    def add(self, *products):
        # Получаем существующие продукты из файла
        existing_products = self.get_products().splitlines()
        # Создаем множество имен существующих продуктов для быстрого поиска
        existing_names = {line.split(', ')[0] for line in existing_products}

        for product in products:
            # Проверяем, есть ли продукт уже в магазине
            if product.name in existing_names:
                print(f"Продукт {product} уже есть в магазине")
            else:
                # Если продукта нет, добавляем его в файл
                with open(self.__file_name, 'a') as file:
                    file.write(str(product) + '\n')

# Пример использования
if __name__ == "__main__":
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # __str__

    s1.add(p1, p2, p3)

    print(s1.get_products())
