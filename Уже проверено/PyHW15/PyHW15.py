from module import *
# Задание 1
# Написать программу «справочник».Создать два списка
# целых. Один список хранит идентификационные коды,
# второй — телефонные номера. Реализовать меню для
# пользователя:
# ■ Отсортировать по идентификационным кодам;
# ■ Отсортировать по номерам телефона;
# ■ Вывести список пользователей с кодами и телефонами;
# ■ Выход.

print()
print('Идентификационные коды:', '\t' * 2,'Номера телефонов:')

########## Как я поняла, идентификационный код это не код города, а именно код номера телефона,
########## поэтому сделала так, как написано в задании. Думаю, разницы нет.

sp_id = []
sp_number = []
label = ['1.', '2.', '3.', '4.', '5.']
users = ['Александр Петров', 'Екатерина Данилова', 'Сергей Орлов', 'Татьяна Степанова', 'Николай Акимов']

for i in range(0, 5):
    show(id(sp_id), number(sp_number))
print()

start = True
while start:
    print('''Что вы хотите сделать со списком?
    1 - Вывести список пользователей с кодами и телефонами;
    2 - Отсортировать по идентификационным кодам;
    3 - Отсортировать по номерам телефона;
    4 - Выйти.''')

    user = int(input("Ваш выбор - "))
    sp_common = list(zip(label, users, sp_id, sp_number))

    if user == 1:
        print(f"\n {' ' * 8} Список пользователей с кодами и телефонами:")
        for i in range(len(users)):
            print(f'{label[i]} {users[i]} - {sp_id[i]} - {sp_number[i]}')

    if user == 2:
        sorted(sp_common, 2, label, 'коду')

    if user == 3:
        sorted(sp_common, 3, label, 'номеру телефона')

    if user == 4:
        start = False
        print("До свидания!")