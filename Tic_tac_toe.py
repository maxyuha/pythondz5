# Создайте программу для игры в ""Крестики-нолики"".

def input_position(): 
    row = int(input('введите номер строки(1-3): '))
    while row < 1 or row > 3:
        row = int(input('введите номер строки (1-3): '))

    columns = int(input('введите номер столбца (1-3): '))
    while columns < 1 or columns > 3:
        columns = int(input('введите номер столбца(1-3): '))

    return row,columns


def check(array):
    if array[0][0] == array[1][0] == array[2][0] != '*':
        return f'выиграл {array[0][0]}'
    elif array[0][1] == array[1][1] == array[2][1] != '*':
        return f'выиграл {array[0][1]}'
    elif array[0][2] == array[1][2] == array[2][2] != '*':
        return f'выиграл {array[0][2]}'
    elif array[0][0] == array[0][1] == array[0][2] != '*':
        return f'выиграл {array[0][0]}'
    elif array[1][0] == array[1][1] == array[1][2] != '*':
        return f'выиграл {array[1][0]}'
    elif array[2][0] == array[2][1] == array[2][2] != '*':
        return f'выиграл {array[2][0]}'
    elif array[0][0] == array[1][1] == array[2][2] != '*':
        return f'выиграл {array[0][0]}'
    elif array[0][2] == array[1][1] == array[2][0] != '*':
        return f'выиграл {array[2][0]}'
    return None

array = [['*','*','*'],['*','*','*'],['*','*','*']]

value = 'X'
i = 0
flag = True
while i < 9 and flag:
    print('\n'.join(['\t'.join(i) for i in array]))
    if i % 2 == 0:
        print('ход крестиков')
        value = 'X'
    else:
        print('ход ноликов')
        value = '0'
    row,columns = input_position()
    if array[row - 1][columns - 1] != '*':
        print('позиция занята')
        row,columns = input_position()

    array[row - 1][columns - 1] = value
    result = check(array)
    if result:
        print(result)
        flag = False
    i += 1