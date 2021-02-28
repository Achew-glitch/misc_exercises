# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла

import re


class Worker:
    def __init__(self, f_str):
        regex_w = r'(?P<Name>\S+) +(?P<Surname>\S+) +(?P<Salary>\d+) +(?P<Position>\S+) +(?P<Rate>\d+)'
        match_w = re.search(regex_w, f_str)
        self.__worker = match_w.groupdict()

    def __str__(self):
        return f'{self.__worker}'

    def __repr__(self):
        return f'{self.__worker}'

    @property
    def clock_rate(self):
        return self.__worker.get('Clock_rate')

    @property
    def name(self):
        return self.__worker.get('Name')

    @property
    def surname(self):
        return self.__worker.get('Surname')

    @property
    def salary(self):
        return self.__worker.get('Salary')

    @property
    def rate(self):
        return self.__worker.get('Rate')

    @clock_rate.setter
    def clock_rate(self, clock_rate_worker):
        if self.__worker.get('Name', 'Surname') == clock_rate_worker.get('Name', 'Surname'):
            self.__worker.update(clock_rate_worker)


workers = []
with open('workers', encoding='UTF-8') as f:
    next(f)
    for worker_read in f:
        workers.append(Worker(worker_read))

with open('hours_of', encoding='utf-8') as hr:
    regex_h = r'(?P<Name>\S+) +(?P<Surname>\S+) +(?P<Clock_rate>\d+)'
    next(hr)
    for hour_read in hr:
        match_h = re.search(regex_h, hour_read)
        for worker in workers:
            worker.clock_rate = match_h.groupdict()

print(f'{"Name":<10} {"Surname":<10} {"Rate":<8} {"Clock_rate":<12} {"Salary":<5}\n')
for worker in workers:
    money = int(worker.salary)
    rate = int(worker.rate)
    clock_rate = int(worker.clock_rate)
    if clock_rate > rate:
        pay = int((2 * money / rate) * (clock_rate - rate) + money)
    else:
        pay = int(money / rate * clock_rate)
    print(f'{worker.name:<10} {worker.surname:<10} {rate:<8} {clock_rate:<12} {pay:<5}')
