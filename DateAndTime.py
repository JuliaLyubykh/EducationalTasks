'''
Написать программу, в которой пользователь вводит временной промежуток в виде
количества дней, часов, минут и секунд, а также узнать общее количество секунд,
составляющих введенный отрезок.
'''
def calculateTime(days, hours, minutes, seconds):
    return days * 86400 + hours * 3600 + minutes * 60 + seconds

def printTime(x):
    return print('Введенный промежуток составляет ', x, ' секунд.')

timelist = input('Введите временной промежуток (число дней, число часов, число минут, число секунд): ').split(', ')
printTime(calculateTime(int(timelist[0]), int(timelist[1]), int(timelist[2]), int(timelist[3])))
