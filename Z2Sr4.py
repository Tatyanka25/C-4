'Zadanie2'
razmerA=int(input('Введите размерность массива A: '))
razmerB=int(input('Введите размерность массива B: '))
A=[0]*razmerA #Заполняем массив А нулями
B=[0]*razmerB #Заполняем массив В нулями
print ('Введите', razmerA, 'элементов массива A:')
for i in range(razmerA): #Перебираем индексы
    A[i]=int(input()) #Вводим числа с клавиатуры
print(A)
print('Введите', razmerB, 'элементов массива В:')
for n in range(razmerB): #Перебираем индексы
    B[n]=int(input()) #Вводим числа с клавиатуры
print(B)
for i in range(razmerA): #Перебираем индексы
    for n in range(razmerB): #Перебираем индексы
        if A[i]==B[n]: #Ищем одинаковые элементы
            print(A[i]) #Выводим одинаковые элементы