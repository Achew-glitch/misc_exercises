# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"
import re


def hours_worked(file):
    regex_h = r'(?P<Имя>\S+) +(?P<Фамилия>\S+) +(?P<Отработано_часов>\d+)'
    h_w = []
    with open(file, encoding='utf-8') as hr:
        next(hr)
        for hour_read in hr:
            match_h = re.search(regex_h, hour_read)
            h_w.append(match_h.groups())
    return h_w


def normative_hours(file):
    regex_w = r'(?P<Имя>\S+) +(?P<Фамилия>\S+) +(?P<Зарплата>\d+) +(?P<Должность>\S+) +(?P<Норма_часов>\d+)'
    workers = []
    with open(file, encoding='utf-8') as wr:
        next(wr)
        for worker_read in wr:
            match_w = re.search(regex_w, worker_read)
            workers.append(match_w.groups())
    return workers

print(f'{"Имя":<10} {"Фамилия":<10} {"Отработано_часов":<5} {"Норматив":<5} {"Зарплата":<5}\n')
for h_workers in hours_worked('hours_of'):
    rate = int(h_workers[2])
    for compare in normative_hours('workers'):
        if h_workers[0] and h_workers[1] in compare:
            money = int(compare[2])
            norm = int(compare[4])
            if rate > norm:
                pay = int((2 * money / norm) * (rate - norm) + money)
            else:
                pay = int(money / norm * rate)
            print(f'{h_workers[0]:<10} {h_workers[1]:<10} {rate:<16} {norm:<8} {pay:<5}')
