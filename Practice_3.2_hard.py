# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"
import re
rate = 200
normative = 40
regex = r'(?P<first_name>\S+) +(?P<last_name>\S+) +(?P<hours>\d+)'
with open('hours_of', encoding='utf-8') as r:
    next(r)
    for read in r:
        match = re.search(regex, read)
        print(match.groups())
        """with open('workers', 'w', encoding='utf-8') as w:
            for employee, hours in reader.items():
                hours = int(hours)
                if 0 < hours <= normative:
                    w.write(f'{employee} - {hours * rate} евро\n')
                elif normative < hours < 252:
                    w.write(f'{employee} - {normative * rate + (hours - normative) * rate * 2} евро\n')
                elif hours >= 252:
                    w.write(f'{employee} скорее всего мертв, так как нельзя отработать больше {hours} часов в неделю\n')
                elif hours <= 0:
                    w.write(f'{employee} не работал вовсе или смог задолжать компании каким-то образом\n')
"""