# Задание 1:
# Пользователь вводит с клавиатуры арифметическое
# выражение. Например, 23+12.
# Необходимо вывести на экран результат выражения.
# В нашем примере это 35. Арифметическое выражение
# может состоять только из трёх частей: число, операция,
# число. Возможные операции: +, -,*,/

x = input("Введите пример через пробел (например: 23 + 15) - ")
x = x.split(' ')
if x[1] == '+':
    print(int(x[0]) + int(x[2]))
if x[1] == '-':
    print(int(x[0]) - int(x[2]))
if x[1] == '*':
    print(int(x[0]) * int(x[2]))
if x[1] == '/':
    print(int(x[0]) / int(x[2]))

# Задание 2:
# В списке целых, заполненном случайными числами,
# определить минимальный и максимальный элементы,
# посчитать количество отрицательных элементов, посчитать количество положительных элементов, посчитать
# количество нулей. Результаты вывести на экран.

l1 = input("Введите числа через пробел - ")
l1 = l1.split(' ')

less0 = 0
more0 = 0
for i in l1:
    if int(i) < 0:
        less0 += 1
    if int(i) > 0:
        more0 += 1

minNum = l1[0]
maxNum = l1[0]
for number in l1:
    if number < minNum:
        minNum = number
    if number > maxNum:
        maxNum = number
print('Максимальное число -', maxNum)
print('Минимальное число -', minNum) # с положительным числами все нормально работает,
# с отрицательными нет. не смогла понять причину :(
print("Количество положительных чисел -", more0)
print("Количество отрицательных чисел -", less0)