'''
Написать программу для отображения стандартной таблицы умножения от единицы
до десяти.
'''
lst0 = ['', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst1 = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst = [lst0, lst1]

for i in range(2, 11):
    lsti = []
    for j in lst1:
        j *= i
        lsti.append(j)
    lst.append(lsti)

for subarr in lst:
    for el in subarr:
        print(el, end=' ')
    print()