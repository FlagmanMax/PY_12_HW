# Задание №3
# Создайте класс-генератор.
# Экземпляр класса должен генерировать факториал числа в
# диапазоне от start до stop с шагом step.
# Если переданы два параметра, считаем step=1.
# Если передан один параметр, также считаем start=1.

class Factorial:
    def __init__(self, stop, start = 1, step = 1):
        self.start = start
        self.stop = stop
        self.step = step

        self.value = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.stop:
            self.value *= self.start
            self.start += self.step
            return self.value
        raise StopIteration

factorial = Factorial(5)
print(*factorial)
