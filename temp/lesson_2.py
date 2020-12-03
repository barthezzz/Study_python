HELP = '''
help - напечатать справку по программе
add - добавить задачу
print - напечатать все задачи
exit - Завершение работы программы
'''

TASKS = list()
while True:
    command = input('Введите команду: ')
    command = command.lower()
    if command == 'help':
        print(HELP)
    elif command == 'add':
        task = input('Введите задачу: ')
        TASKS.append(task)
        print(f'Задача {task} добавлена!')
    elif command == 'print':
        for task in TASKS:
            print(task)
    elif command == 'exit':
        print('Спасибо за использование! До свидания!')
        break
    else:
        print('Неизвестная команда')
        break