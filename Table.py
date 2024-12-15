'''
Программа должна вывести фрагмент таблицы умножения для всех чисел отрезка
[a;b] на все числа отрезка [c;d].

'''
a =int (input())
b =int (input())
c =int (input())
d =int (input())
for i in range (c,d+1):
    print('\t'+str(i),end='')
print(end='\n')
for i in range (a,b+1):
    print(str(i)+'\t',end='')
    for j in range (c,d+1):
        print(str(i*j),end='\t')
    print(end='\n')
