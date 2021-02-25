# -*- coding: utf-8 -*-
# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# (done) 1. Получить полный список всех классов школы
# (done) 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

from random import randint


class School:
    groups = []
    number = randint(1, 500)

    def __str__(self):
        return f'Список классов в школе {self.number}: {self.groups}'

    def add_group(self, add_gr):
        if isinstance(add_gr, Group):
            self.groups.append(add_gr)
        else:
            print(f'{add_gr} такого класса не может быть')

    def get_group(self, get_gr):
        for el in self.groups:
            if el.group == get_gr:
                return el
        else:
            print(f'В школе {self.number} нет класса {get_gr}')


class Group():
    def __init__(self, group):
        self.group = group
        self.students = []
        self.teachers = []

    def __str__(self):
        return self.group

    def __repr__(self):
        return self.group

    def add_teacher(self, add_tc):
        if isinstance(add_tc, Teacher):
            self.teachers.append(add_tc)
        else:
            print(f'{add_tc} не является учеником')

    def add_student(self, add_st):
        if isinstance(add_st, Student):
            self.students.append(add_st)
        else:
            print(f'{add_st} не является учеником')

    def get_students(self):
        print(f'Список учеников в классе {self.group}:')
        for get_st in self.students:
            print(get_st)

    def get_teachers(self):
        print(f'Список учелей класса {self.group}:')
        for get_tc in self.teachers:
            print(get_tc)

    def get_subjects(self):
        get_sb = []
        for tc in self.teachers:
            get_sb.append(tc.subject)
        return get_sb


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


class Student(People):
    def __init__(self, group, name, surname, mom, dad):
        super().__init__(name, surname, mom, dad)
        self.gr = group

    def __str__(self):
        return f'{self.name} {self.surname} из класса {self.gr.group}\n' \
               f'Родители: {self.parents}'

    def get_subjects(self):
        return f'Список предметов: {self.gr.get_subjects()}'


class Teacher(People, Group):
    def __init__(self, subject, group, name, surname):
        super().__init__(name, surname)
        self.subject = subject
        self.group = group

    def __str__(self):
        return f'{self.name} {self.surname} преподает {self.subject}'


sc = School()
for i in range(1, 15):
    gr = Group(f"{randint(1, 11)}{chr(randint(ord('А'), ord('ж')))}")
    sc.add_group(gr)

i = 0
while i < 71:
    for gr in sc.groups:
        c = chr(randint(ord('А'), ord('Я')))
        gr.add_student(Student(name=c, surname=c, mom=c, dad=c, group=gr))
        i += 1

i = 0
sj = ['Математика', 'Физика', 'Литература', 'Язык', 'Правоведение', 'Химия',
      'Физкультура', 'География', 'Информатика']

for gr in sc.groups:
    if not gr.teachers:
        for i in range(1, randint(1, 4)):
            c = chr(randint(ord('a'), ord('z')))
            r_sj = sj[randint(0, len(sj) - 1)]
            tc = Teacher(name=c, surname=c, subject=r_sj, group=gr)
            gr.add_teacher(tc)

while True:
    print(sc)
    a = input('Класс: ')
    if a == 'выход':
        break
    elif a:
        c_gr = sc.get_group()
        c_gr.get_students()
        a = input('Ученик: ')
        if a == 'выход':
            break
        elif a:
            pass