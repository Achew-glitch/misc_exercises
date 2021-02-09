# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruits_1 = ['apple', 'orange', 'watermelon', 'peach']
fruits_2 = ['pear', 'orange', 'peach', 'watermelon', 'grape']

print(f'fruits_1: {fruits_1}\nfruits_2: {fruits_2}')
cross_list = [cross_fruit for cross_fruit in fruits_1 if cross_fruit in fruits_2]
print(f'crossing fruits of lists: {cross_list}')