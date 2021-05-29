
# Создаем базовый класс Фигуры
class Figure:
    __area = 0
    __perimeter = 0

    def __init__(self, name, angles):
        self.name = name,
        self.angles = angles

    @property
    def area(self):
        return self.__area

    @property
    def perimeter(self):
        return self.__perimeter

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return self.area + figure.area
        raise AssertionError('Объект не является фигурой')


# Создаем класс Треугольник, потомок класса Фигуры
class Triangle(Figure):
    name = "triangle"
    angles = 3

    def __init__(self, base, height, side_a, side_b, side_c):
        self.base = base
        self.height = height
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    # Задаем функцию подсчета площади треугольника
    @property
    def area(self):
        return 0.5 * self.base * self.height

    # Задаем функцию подсчета периметра треугольника
    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c


# Создаем переменную треугольник
triangle = Triangle(base=1, side_b=4, height=5, side_a=1, side_c=2)


# Создаем класс Квадрат, потомок класса Фигуры
class Rectangle(Figure):
    name = "Rectangle"
    angles = 4

    def __init__(self, height, width):
        self.height = height
        self.width = width

    # Задаем функцию подсчета площади прямоугольника
    @property
    def area(self):
        return self.width * self.width * 2

    # Задаем функцию подсчета периметра прямоугольника
    @property
    def perimeter(self):
        return (self.width + self.height) * 2


# Создаем переменную прямоугольник
rectangle = Rectangle(height=1, width=3)


# Создаем класс Квадрат
class Square(Rectangle):
    name = "Square"
    angles = 4

    def __init__(self, side):
        self.side = side

    # Задаем функцию подсчета периметра квадрата
    @property
    def perimeter(self):
        return 4 * self.side

    # Задаем функцию подсчета площади квадрата
    @property
    def area(self):
        return self.side * self.side


# Создадим переменную квадрат
square = Square(side=3)


class Circle(Figure):
    name = "Circle"
    angles = 0

    def __init__(self, radius):
        self.radius = radius

    # Высчитываем площадь круга
    @property
    def area(self):
        return 3.14 * self.radius ** 2


circle = Circle(radius=3)
