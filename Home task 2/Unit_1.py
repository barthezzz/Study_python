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