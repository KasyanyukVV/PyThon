class Animal:
    alive = True  # (живой)         перенесен из фукции __init__
    fed = False  # (накормленный)   перенесен из фукции __init__
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if isinstance(food, Plant): # добавлен isinstance к функции
            if food.edible:
                print(f"{self.name} съел {food.name}")
                self.fed = True
            else:
                print(f"{self.name} не стал есть {food.name}")
                self.alive = False


class Plant:
    edible = False  # (съедобность) перенесен из фукции __init__
    def __init__(self, name):
        self.name = name

# Классы наследники
class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Flower(Plant):
    pass


class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True


# Создание объектов классов
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

# Выполнение действий
print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)


