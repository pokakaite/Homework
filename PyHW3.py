# Задание 1. Пользователь вводит с клавиатуры три цифры. Необходимо создать число, содержащее эти цифры. Например,
# если с клавиатуры введено 1, 5, 7, тогда нужно сформировать число 157.

x = (input("Введите число - "))
y = (input("Введите число - "))
z = (input("Введите число - "))

print(int(x + y + z))

# Задание 2. Пользователь вводит с клавиатуры число, состоящее
# из четырех цифр. Требуется найти произведение цифр.
# Например, если с клавиатуры введено 1324, тогда результат произведения 1 * 3 * 2 * 4 = 24

num = int(input("Введите четырёхзначное число - "))
x = num // 1000
y = (num // 100) % 10
z = (num // 10) % 10
k = num % 10

print(x * y * z * k)

# Задание 3. Пользователь вводит с клавиатуры количество метров. Требуется вывести результат перевода
# метро в сантиметры, дециметры, миллиметры, мили.

metres = int(input("Введите количество метров - "))
sm = metres * 100
dm = metres / 10
mm = metres * 1000
miles = metres * 1609.344
print("Сантиметры -", sm)
print("Дециметры", dm)
print("Миллиметры",mm)
print("Мили", miles)

# Задание 4. Напишите программу, вычисляющую площадь треугольника. Пользователь с клавиатуры вводит размер
# основания треугольника и размер высоты.

a_tr = int(input("Введите длину основания треугольника - "))
h_tr = int(input("Введите длину высоты треугольника - "))
S = 0.5 * a_tr * h_tr
print("Площадь треугольника -", S)

# Задание 5. Пользователь с клавиатуры вводит четырёхзначное
# число. Необходимо перевернуть число и отобразить
# результат. Например, если введено 4512, результат 2154.

num = int(input("Введите четырёхзначное число - "))
x = num % 10
y = (num % 100) // 10
z = (num % 1000) // 100
k = num // 1000

print(x, y, z, k, sep='')








