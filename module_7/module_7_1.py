# -*- coding: utf-8 -*-


class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self) -> str:
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self) -> None:
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        products = file.read()
        file.close()
        return products

    def add(self, *products):
        file = open(self.__file_name, 'a')
        products_in_shop = self.get_products()
        for product in products:
            if product.name in products_in_shop:
                print(f'Продукт {product} уже есть в магазине')
            else:
                file.write(f'{product.__str__()}\n')
        file.close()


if __name__ == '__main__':
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2) # __str__

    s1.add(p1, p2, p3)

    print(s1.get_products())
    
    # Вывод на консоль:
    '''
    Первый запуск:
    Spaghetti, 3.4, Groceries
    Potato, 50.5, Vegetables
    Spaghetti, 3.4, Groceries
    Potato, 5.5, Vegetables
    
    Второй запуск:
    Spaghetti, 3.4, Groceries
    Продукт Potato, 50.5, Vegetables уже есть в магазине
    Продукт Spaghetti, 3.4, Groceries уже есть в магазине
    Продукт Potato, 5.5, Vegetables уже есть в магазине
    Potato, 50.5, Vegetables
    Spaghetti, 3.4, Groceries
    Potato, 5.5, Vegetables
    '''

