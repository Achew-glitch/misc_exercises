# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

from random import randint


class People:
    parents = []

    def __init__(self, name, surname, mom=None, dad=None):
        self.name = name
        self.surname = surname
        if isinstance(self, Student):
            try:
                self.parents = People(name=mom, surname=self.surname), People(name=dad, surname=self.surname)
            except TypeError:
                print('Не укаано имя\имена родителей')

    def __str__(self):
        return f'{self.name} {self.surname}'

    def __repr__(self):
        return f'{self.name} {self.surname}'


class School:
    groups = []
    number = randint(1, 500)

    def __str__(self):
        return f'Список классов в школе {self.number}: {self.groups}'

    def add_group(self, group):
        if isinstance(group, Group):
            self.groups.append(group)
        else:
            print(f'{group} такого класса не может быть')


class Student(People):
    def __init__(self, group, name, surname, mom, dad):
        super().__init__(name, surname, mom, dad)
        self.group = group

    def __str__(self):
        return f'{self.name} {self.surname} из класса {self.group}\n' \
               f'Родители: {self.parents}\n' \
               f'Список предметов: {self.subjects}'

    def change_group(self, group):
        self.group = group

    def set_subjects(self, *args):
        self.subjects = args


class Teacher(People):
    def __init__(self, subject, group, name, surname):
        super().__init__(name, surname)
        self.subject = subject
        self.group = group

    def __str__(self):
        return f'{self.name} {self.surname} преподает {self.subject}'


class Group(School):
    students = []
    teachers = []

    def __str__(self):
        return self.group

    def __repr__(self):
        return self.group

    def __init__(self, group):
        self.group = group

    def add_teacher(self, teacher):
        if isinstance(teacher, Teacher):
            self.teachers.append(teacher)
        else:
            print(f'{teacher} не является учеником')

    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)
        else:
            print(f'{student} не является учеником')

    def get_students(self):
        print(f'Список учеников в классе {self.group}:')
        for student in self.students:
            print(student)



sc = School()
for i in range(1, 15):
    gr = Group(f"{randint(1, 11)}{chr(randint(ord('А'), ord('З')))}")
    sc.add_group(gr)
print(sc)
a = input('Укажите класс: ')
sc.groups[a].get_students()
