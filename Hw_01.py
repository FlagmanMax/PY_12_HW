# Создайте класс студента.
# ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и
# наличие только букв.
# ○ Названия предметов должны загружаться из файла CSV при создании
# экземпляра. Другие предметы в экземпляре недопустимы.
# ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
# тестов (от 0 до 100).
# ○ Также экземпляр должен сообщать средний балл по тестам для каждого
# предмета и по оценкам всех предметов вместе взятых.
import csv

class Range:
    """
    Class for checking low and high limits of input values
    """
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
            raise ValueError("Value is lower than low limit")
        if self.max_value is None or value > self.max_value:
            raise ValueError("Value is higher than high limit")

class Text:
    """
    Class for checking input strings in names
    """
    def __init__(self, title_check, alpha_check):
        self.title_check = title_check
        self.alpha_check = alpha_check

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __set__(self, instance, value):
        if self.alpha_check(value):
            if self.title_check(value):
                setattr(instance, self.param_name, value)
            else:
                raise ValueError(f'Bad name "{value}": name should start with a title character')
        else:
            raise ValueError(f'Bad name "{value}": name should have only characters')

class Marks_book:
    """
    Class for saving marks and test results for each student
    """
    def __init__(self, subjects_tuple):
        self.dict_mark = {}
        for subject in subjects_tuple:
           self.dict_mark[subject] = []

        self.dict_test_result = {}
        for subject in subjects_tuple:
            self.dict_test_result[subject] = []

    def add_mark(self, subject_string, subject_mark):
        self.dict_mark[subject_string].append(subject_mark)

    def add_test_result(self, subject_string, subject_test_result):
        self.dict_test_result[subject_string].append(subject_test_result)

    def print_mark(self, subject_string):
        print(*self.dict_mark.get(subject_string))

    def print_test_result(self, subject_string):
        print(*self.dict_test_result.get(subject_string))

    def ave_test_result_per_subject(self):
        print("Средняя оценка за тесты:")
        for subject in self.dict_test_result.keys():
            if len(self.dict_test_result[subject]) == 0:
                result = f"нет оценок"
            else:
                ave = 0
                count = 0
                for value in self.dict_test_result[subject]:
                    ave += int(value)
                    count += 1
                result = f"{round(ave/count,2)}"
            print(f"\t{subject}: \t{result}")

    def get_ave_mark(self):
        ave = 0
        count = 0
        result = "нет оценок"
        for subject in self.dict_mark.keys():
            if len(self.dict_mark[subject]) != 0:
                for value in self.dict_mark[subject]:
                    ave += int(value)
                    count += 1
                result = f"{round(ave / count, 2)}"
        print(f"Средняя оценка:\t{result}")

class Student:
    """
    Main class for a student
    """
    first_name = Text(str.istitle, str.isalpha)
    middle_name = Text(str.istitle, str.isalpha)
    second_name = Text(str.istitle, str.isalpha)

    _mark = Range(2, 5)
    _test_result = Range(0, 100)

    def __init__(self, first_name, middle_name, second_name, ):
        self.first_name = first_name
        self.middle_name = middle_name
        self.second_name = second_name
        self._subjects = ()
        self.__get_subjects()

        self.mb = Marks_book(self._subjects)

    def __str__(self):
        return f'{self._first_name} {self._middle_name} {self._second_name}'

    @property
    def subjects(self):
        return self._subjects

    def __get_subjects(self, path: str= 'Hw_01.csv'):
        temp_list = []
        with open(path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file, dialect='excel', delimiter=';')
            for row in reader:
                temp_list.append(*row)
            self._subjects = tuple(temp_list)

    def add_mark(self, subject_str, mark):
        self._mark = mark
        if subject_str in self._subjects:
            self.mb.add_mark(subject_str,mark)
        else:
            print(f"Нет такого предмета '{subject_str}' в программе обучения студента")

    def print_mark(self,subject_str):
        if subject_str in self._subjects:
            print(f"Студент {self._second_name} {self._first_name} имеет следующие оценки по {subject_str}: ")
            self.mb.print_mark(subject_str)
        else:
            print(f"Нет такого предмета '{subject_str}' в программе обучения студента")

    def add_test_result(self, subject_str, test_result):
        self._test_result = test_result
        if subject_str in self._subjects:
            self.mb.add_test_result(subject_str,test_result)
        else:
            print(f"Нет такого предмета '{subject_str}' в программе обучения студента")

    def print_test_result(self,subject_str):
        if subject_str in self._subjects:
            print(f"Студент {self._second_name} {self._first_name} имеет следующие результаты тестирования по {subject_str}: ")
            self.mb.print_test_result(subject_str)
        else:
            print(f"Нет такого предмета '{subject_str}' в программе обучения студента")

    def print_ave_test_result(self):
        self.mb.ave_test_result_per_subject()

    def print_ave_mark(self):
        self.mb.get_ave_mark()


student_01 = Student('Иван','Иванович','Иванов')
print(student_01)
print(*student_01.subjects)

student_01.add_mark("Математика",5)
student_01.add_mark("Математика",4)
student_01.add_mark("Математика",3)
student_01.print_mark("Математика")

student_01.add_test_result("Математика",100)
student_01.add_test_result("Математика",90)
student_01.add_test_result("Математика",80)
student_01.print_test_result("Математика")

student_01.add_test_result("Математи",3)

student_01.print_ave_test_result()
student_01.print_ave_mark()



