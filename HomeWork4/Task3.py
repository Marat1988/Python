class Triangle:

    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_side_a(self):
        return self.side_a

    def get_side_b(self):
        return self.side_b

    def get_side_c(self):
        return self.side_c

# Сделал по-другому. Класс TriangeChecker у меня принимает треугольник
# И далее в методе is_triangle класса TriangeChecker идет проверка, согласно заданию.
class TriangleChecker:
    def __init__(self, triangle):
        self.triangle = triangle

    def is_triangle(self):
        if not (isinstance(self.triangle, Triangle)):
            return "Вы передали не треугольник"
        if self.triangle.get_side_a() <= 0 or self.triangle.get_side_b() <= 0 or self.triangle.get_side_c() <= 0:
            return "Отрицательные значение сторон треугольника или значения равное нулю недопустимы"
        if (not (isinstance(self.triangle.get_side_a(), int))
                or not (isinstance(self.triangle.get_side_b(), int))
                or not (isinstance(self.triangle.get_side_c(), int))):
            return "Допустимы только числа"
        if ((self.triangle.get_side_a() + self.triangle.get_side_b() > self.triangle.get_side_c())
                and (self.triangle.get_side_a() + self.triangle.get_side_c() > self.triangle.get_side_b())
                and (self.triangle.get_side_b() + self.triangle.get_side_c() > self.triangle.get_side_a())):
            return "Треугольник может существовать"
        return "Треугольник не возможно построить"


triangle1 = Triangle(4, 5, 6)
triangle_checker1 = TriangleChecker(triangle1)
print(triangle_checker1.is_triangle())

triangle2 = Triangle(1, 5, 6)
triangle_checker2 = TriangleChecker(triangle2)
print(triangle_checker2.is_triangle())
