# date = input('Введите дату: ')

# if (date == 'Завтра'):
#     print('Завтра 2 декабря')
# else:
#     print('Есть только один день - Завтра')

# date = input('Введите число: ')

# date = int(date)

# if date > 100:
#     print('Очень большое число!')
# elif date % 2 == 0:
#     print('Четное число')
# elif date % 3 == 0:
#     print('Делится на 3 ')
# else:
#     print('Какое-то плохое число!')


# x = True
# y = False
#print(not y)
#print(x or y)

login = input('Введите логин: ')

if login != '' and (login == 'admin' or login = admin1):
    print('Темная тема включена')
else:
    print('Извните, у вас нет доступа к темной теме')


HELP = '''
help - напечатать справку по программе
add - добавить задачу
print - напечатать все задачи
exit - Завершение работы программы
'''

TASKS = []
while True:
    command = input('Введите команду: ')
    command = command.lower()
    if command == 'help':
        print(HELP)
    elif command == 'add':
        task = input('Введите задачу: ')
        TASKS.append(task)
        print('Задача добавлена!')
    elif command == 'print':
        print(TASKS)
    elif command == 'exit':
        print('Спасибо за использование! До свидания!')
        break
    else:
        print('Неизвестная команда')
        break