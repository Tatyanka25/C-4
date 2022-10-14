'Zadanie2'
razmerA=int(input('Введите размерность массива A: '))
razmerB=int(input('Введите размерность массива B: '))
A=[0]*razmerA #Заполняем массив А нулями
B=[0]*razmerB #Заполняем массив В нулями
print ('Введите', razmerA, 'элементов массива A:')
A=[int(input()) for i in range(razmerA)] #Заполняем массив A элементами с клавиатуры
print(A)
print('Введите', razmerB, 'элементов массива В:')
B=[int(input()) for n in range(razmerB)] #Заполняем массив B элементами с клавиатуры
print(B)
print(set(A) & set(B)) #Выводим общие элементы