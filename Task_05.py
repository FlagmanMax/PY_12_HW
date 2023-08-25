# Задание №5
# Доработаем прямоугольник и добавим экономию памяти
# для хранения свойств экземпляра без словаря __dict__.

# Задание №4 s_12
# Доработайте класс прямоугольник из прошлых семинаров.
# Добавьте возможность изменять длину и ширину
# прямоугольника и встройте контроль недопустимых значений
# (отрицательных).
# Используйте декораторы свойств.

# адание №6 s_11
# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения

# @total_ordering
class Rectangle():
    __slots__ = ('_a', '_b')

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return Rectangle(self.a + other.a, self.b+other.b)
        return NotImplemented

    def __init__(self, a, b=None):
        self._a = a
        if b is None:
            self._b = a
        else:
            self._b = b

    def get_square(self):
        return self._a * self._b

    def get_length(self):
        return 2 * (self._a + self._b)

    def __repr__(self):
        return f"Rectangle({self._a}, {self._b})"

    def __sub__(self, other):
        if isinstance(other, Rectangle):
            if other._a > self._a or other._b > self._b:
                raise ValueError("Ошибка!")
            return Rectangle(self._a - other._a, self._b-other._b)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.get_square() == other.get_square()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Rectangle):
            return self.get_square() > other.get_square()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Rectangle):
            return self.get_square() >= other.get_square()
        return NotImplemented

    @property
    def a(self, value):
        return self._a

    @a.setter
    def a(self, value):
        if value > 0:
            self._a = value
        else:
            raise ValueError("Error")

    @property
    def b(self, value):
        return self._b

    @a.setter
    def b(self, value):
        if value > 0:
            self._b = value
        else:
            raise ValueError

# rectangle1 = Rectangle(3)
# print(f'{rectangle1=}')
#
# rectangle2 = Rectangle(2,3)
# print(f'{rectangle2=}')
#
# rectangle3 = rectangle1 + rectangle2
# print(rectangle3)
#
# rectangle4 = rectangle1 - rectangle2
# print(rectangle4)
#
# print(rectangle1>rectangle2)
# print(rectangle1<rectangle2)
# print(rectangle1>=rectangle2)
# print(rectangle1<=rectangle2)
# print(rectangle1==rectangle2)
# print(rectangle1!=rectangle2)

obj_a = Rectangle(5,6)
print(obj_a)
obj_a.a = 6
print(obj_a)

try:
    obj_a.a = -10
except ValueError as e:
    print(e)