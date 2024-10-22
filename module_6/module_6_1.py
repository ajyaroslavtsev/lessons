# -*- coding: utf-8 -*-


class Animal:
    '''Класс животные'''

    def __init__(self, name):
        self.name = name        
        self.alive = True  # живой
        self.fed = False      # накормленный

    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Plant:
    '''Класс растения'''

    def __init__(self, name, edible = False):
        self.name = name        
        self.edible = edible  # съедобность


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Flower(Plant):
    pass


class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name, edible=True)


if __name__ == '__main__':
    a1 = Predator('Волк с Уолл-Стрит')
    a2 = Mammal('Хатико')
    p1 = Flower('Цветик семицветик')
    p2 = Fruit('Заводной апельсин')

    print(a1.name)
    print(p1.name)

    print(a1.alive)
    print(a2.fed)
    a1.eat(p1)
    a2.eat(p2)
    print(a1.alive)
    print(a2.fed)

    # Вывод на консоль:
    '''
    Волк с Уолл-Стрит
    Цветик семицветик
    True
    False
    Волк с Уолл-Стрит не стал есть Цветик семицветик
    Хатико съел Заводной апельсин
    False
    True
    '''
