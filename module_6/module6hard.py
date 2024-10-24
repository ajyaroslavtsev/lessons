# -*- coding: utf-8 -*-

from math import pi, sqrt


class Figure:
    '''Геометрическая Фигура - базовый класс'''
    sides_count = 0  # - число сторон

    def __init__(self, color, *sides):
        if not isinstance(color, tuple) and len(color) == 3:
            raise ValueError("Недопустимые значения цвета.")
        self.__color = list(color)           # - список цветов в формате RGB

        self.__sides = sides                 # - список сторон
        if len(sides) == self.sides_count:
            self.__sides = list(sides)
        elif len(sides) > 1:
            self.__sides = list([1] * self.sides_count)
        else:
            self.__sides = list(sides * self.sides_count)

        self.filled = True                   # - закрашенный, bool

    def get_color(self):
        '''Возвращает список RGB цветов.'''
        return self.__color

    def __is_valid_color(self, r, g, b):
        '''Метод __is_valid_color - служебный, принимает параметры r, g, b, 
        и проверяет корректность переданных значений перед установкой нового цвета. 
        Корректным считается цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 
        (включительно)
        '''
        return all(isinstance(value, int) and 0 <= value <= 255 for value in (r, g, b))

    def set_color(self, r, g, b):
        '''Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color 
        на соответствующие значения, предварительно проверив их на корректность. Если введены 
        некорректные данные, то цвет остаётся прежним
        '''
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
    
    def __is_valid_sides(self, *sides):
        '''Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон, 
        возвращает True если все стороны целые положительные числа и кол-во новых сторон 
        совпадает с текущим, False - во всех остальных случаях.
        '''
        # Проверяем, что количество новых сторон совпадает с текущим
        if len(sides) != self.sides_count:
            return False
        # Проверяем, что все стороны - целые положительные числа
        return all(isinstance(side, int) and side > 0 for side in sides)

    def get_sides(self):
        '''Возвращать значение атрибута __sides.'''
        return self.__sides

    def __len__(self):
        '''Возвращает периметр фигуры.'''
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        '''Метод set_sides(self, *new_sides) должен принимать новые стороны, если их 
        количество не равно sides_count, то не изменять, в противном случае - менять.
        '''
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    '''Круг - является фигурой'''
    sides_count = 1

    def get_radius(self):
        '''Возвращает радиус круга.'''
        self.__radius = super().get_sides()[0] / (2 * pi)
        return self.__radius

    def get_square(self):
        '''Возвращает площадь круга.'''
        return pi*(self.__radius**2)


class Triangle(Figure):
    '''Триугольник - является фигурой'''
    sides_count = 3

    def get_square(self):
        '''Возвращает площадь треугольника.'''
        p_perimeter = super().__len__() / 2 # полупериметр
        a, b, c = super().get_sides()
        return sqrt(p_perimeter * (p_perimeter - a) * (p_perimeter - b) * (p_perimeter - c))


class Cube(Figure):
    '''Куб - является фигурой'''
    sides_count = 12

    def get_volume(self):
        '''Возвращает объём куба.'''
        return self.get_sides()[0]**3


if __name__ == '__main__':
    circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77) # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15) # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15) # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())

    # Вывод на консоль:
    '''
    [55, 66, 77]
    [222, 35, 130]
    [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
    [15]
    15
    216
    '''