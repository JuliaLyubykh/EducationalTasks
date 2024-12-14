'''
Написать программу, которая будет случайным образом подбирать шесть номеров
для лотерейного билета. Необходимо убедиться, что в числах нет дубликатов
Вывести номера билетов на экран по возрастанию.
'''

# Для главного приза требуется, чтобы 6 номеров на лотерейном билете
# совпали с 6 случайным образом подобранными в диапазоне от 1 до 49.

import random

def create_random_numbers():
    numbers = random.sample(range(1,50), 6)
    numbers.sort()
    return numbers

mainPrize = random.sample(range(1,50), 6)
numbers = create_random_numbers()

print(mainPrize)
print(numbers)

if numbers == mainPrize:
    print("Вы выиграли!")
else: 
    print("Не совпало!")
