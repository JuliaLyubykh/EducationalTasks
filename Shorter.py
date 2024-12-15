'''
Напишите программу, которая считывает строку, кодирует её предложенным
алгоритмом и выводит закодированную последовательность на стандартный
вывод.
'''

# Формат вывода: s = 'aaaabbсaa' преобразуется в 'a4b2с1a2'
s = input()
length = len(s)-1
count = 1
tab = ''
if len(s)==1:
    tab = tab + s + str(count)
else:
    for i in range(0,length):
        if s[i]==s[i+1]:
            count +=1
        elif s[i]!=s[i+1]:
            tab = tab + s[i]+str(count)
            count = 1
    for j in range(length,length+1):
        if s[-1]==s[-2]:
            tab = tab +s[j]+str(count)
        elif s[-1]!=s[-2]:
            tab = tab +s[j]+str(count)
            count = 1
print(tab)
