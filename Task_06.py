# Задание №6
# Изменяем класс прямоугольника.
# Заменяем пару декораторов проверяющих длину и ширину
# на дескриптор с валидацией размера.
class Range:
    def __init__(self, min_value=None, max_value=None ):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = '_'+ name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance,self.param_name, value)

    def validate(self, value):
        if self.min_value is None or value < self.min_value:
            raise ValueError("Error")
        if self.max_value is None or value > self.max_value:
            raise ValueError("Error")




class Rectangle:
    _a = Range(0, 100)
    _b = Range(0, 100)

    def __init__(self, a, b=None):
        self._a = a
        if b is None:
            self._b = a
        else:
            self._b = b

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return Rectangle(self.a + other.a, self.b+other.b)
        return NotImplemented

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

obj_a = Rectangle(5,100)
print(obj_a)
obj_a.a = 6
print(obj_a)


