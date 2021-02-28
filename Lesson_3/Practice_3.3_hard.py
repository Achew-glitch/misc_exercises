# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

with open('fruits.txt', encoding='utf-8') as r:
    for char in list(map(chr, range(ord('а'), ord('я')+1))):
        founding_fruits = ''
        for word in r:
            if word.lower().startswith(char):
                founding_fruits += word
            elif word == '\n':
                continue
        r.seek(0)
        name_file = 'fruits_' + char
        with open(name_file, 'w', encoding='utf-8') as w:
            w.write(founding_fruits)
