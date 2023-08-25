# Задание №2
# Доработаем задачу 1.
# Создайте менеджер контекста, который при выходе
# сохраняет значения в JSON файл.

# Задание №1
# Создайте класс-функцию, который считает факториал числа при
# вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и
# их факториалов.
import json

class Factorial:
    _instance = None


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

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.res = dict(zip(self._arg_archive, self._num_archive))
        self.json_file = open("Task_02.json", 'w')
        json.dump(self.res, self.json_file, indent=2)
        self.json_file.close()


factorial = Factorial()
with factorial as fac:
    print(fac(3))
    print(fac(4))
    print(fac(5))
print(factorial.number_archive())