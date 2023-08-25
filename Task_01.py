# Задание №1
# Создайте класс-функцию, который считает факториал числа при
# вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и
# их факториалов.

class Factorial:
    _instance = None

    # def __new__(cls, *args, **kwargs):
    #     if cls._instance is None:
    #         cls._instance = super().__new__(cls)
    #         cls._instance._arg_archive = []
    #         cls._instance._num_archive = []
    #         cls._instance._factorial = 1
    #     return cls._instance
    def __init__(self):
        self._arg_archive = []
        self._num_archive = []
        self._factorial = 1

    def __call__(self, num):
        self._arg_archive.append(num)
        self.num = num
        factorial = 1
        for i in range(num):
            factorial *= (i+1)
        self._num_archive.append(factorial)
        return factorial

    def __str__(self):
        return f'{self._arg_archive}, {self._num_archive}'

    def number_archive(self):
        return self._arg_archive, self._num_archive

factorial = Factorial()
print(factorial(3))
print(factorial(4))
print(factorial(5))
print(factorial.number_archive())