# # Задание 1. Пользователь вводит с клавиатурытри числа. Необходимо найти сумму чисел,
# # произведение чисел. Результат вычислений вывести на экран.

x = int(input("Введите число - "))  # 10
y = int(input("Введите число - "))  # 20
z = int(input("Введите число - "))  # 30
print("Сумма чисел равна -", (x + y + z))  # 60
print("Произведение чисел равно -", (x * y * z))  # 6000

# # Задание 2. Пользователь вводит с клавиатуры три числа. Первое
# # число — зарплата за месяц, второе число — сумма месячного платежа по кредиту в банке, третье число —
# # задолженность за коммунальные услуги. Необходимо вывести
# # на экран сумму, которая останется у пользователя после всех выплат.

x = int(input("Введите зарплату за месяц - "))  # 30000
y = int(input("Введите сумму ежемесячного платежа по кредиту в банке - "))  # 5000
z = int(input("Введите сумму задолженности за коммунальные услуги - "))  # 10000
print("После всех выплат у вас останется -", (x - y - z), "рублей")  # 15000

# # Задание 3. Напишите программу, вычисляющую площадь ромба.
# # Пользователь с клавиатуры вводит длину двух его диагоналей.

x = int(input("Введите длину первой диагонали - "))  # 10
y = int(input("Введите длину второй диагонали - "))  # 20
print("Площадь ромба равна -", ((x * y) / 2))  # 100

# Задание 4. Выведите на экран надпись To be or not to be
# на разных строках. Пример вывода:
# To be
# or not
# to be

print("To be", "or not", "to be", sep='\n')

# Задание 5. Выведите на экран надпись «Life is what happens when
# you're busy making other plans» John Lennon на разных
# строках. Пример вывода:
# “Life is what happens
#         when
#       you’re busy making other plans”
#                                      John Lennon.

print('"Life is what happens', "   when", '      you\'re busy making other plans"', "         John Lennon.", sep='\n')