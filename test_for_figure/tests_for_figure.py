from extra.hw_1 import triangle, rectangle,square,circle
# Тесты на треугольник
def test_perimetr_triangle():
    assert triangle.perimeter == 7


def test_add_area_triangle_rectangle():
    assert triangle.add_area(rectangle) == 20.5


def test_add_area_triangle_triangle():
    assert triangle.add_area(triangle) == 5


def test_add_area_triangle_square():
    assert triangle.add_area(square) == 11.5


def test_add_area_triangle_circle():
    assert triangle.add_area(circle) == 30.76


# Тесты на прямоугольник
def test_angles_rectangle():
    assert rectangle.angles == 4


def test_perimeter_rectangle():
    assert rectangle.perimeter == 8


def test_add_area_rectangle_triangle():
    assert rectangle.add_area(triangle) == 20.5


def test_add_area_rectangle_rectangle():
    assert rectangle.add_area(rectangle) == 36


def test_add_area_rectangle_square():
    assert rectangle.add_area(square) == 12


def test_add_area_rectangle_square():
    assert rectangle.add_area(circle) == 46.260000000000005


# Тесты на квадрат
def test_angles_square():
    assert square.angles == 4


def test_perimeter_square():
    assert square.perimeter == 12


def test_add_square_square():
    assert square.add_area(square) == 18


def test_add_square_triangle():
    assert square.add_area(triangle) == 11.5


def test_add_square_rectangle():
    assert square.add_area(rectangle) == 27


def test_add_square_circle():
    assert square.add_area(circle) == 37.260000000000005


# Тесты на круг
def test_angles_circle():
    assert circle.angles == 0


def test_add_circle_circle():
    assert circle.add_area(circle) == 56.52


def test_add_circle_triangle():
    assert circle.add_area(triangle) == 30.76


def test_add_circle_rectangle():
    assert circle.add_area(rectangle) == 46.260000000000005


def test_add_circle_square():
    assert circle.add_area(square) == 37.260000000000005
