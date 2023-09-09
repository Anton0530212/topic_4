# Программа, которая запрашивает у пользователя два числа
# и выводит сообщение, соответствует ли условие boolian()
first_number: float = float(input('Введите первое число: '))
second_number: float = float(input('Введите второе число: '))

result = bool(first_number > second_number)

print('Число', first_number, 'больше числа', second_number, 'это -', result)
