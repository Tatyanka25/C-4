'Zadanie1'
razmer=int(input('Введите размерность массива: '))
C=[0] * razmer #Заполняем массив нулями
from random import uniform #Подключаем функцию uniform
for i in range(razmer): #Перебираем индексы
    C[i]=uniform(1,155) #Случайные числа от 1 до 155
print('Исходный массив:', C) 
for i in range(razmer): #Перебираем индексы
    if C[i]==max(C):  #Находим максимальный элемент
        for i in range(i+1, razmer): #Перебираем индексы
            C[i]=0  #Делаем все элементы массива, стоящие после максимального элемента, нулями
print('Конечный массив:', C)