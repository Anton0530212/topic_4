# Программа которая выводит белево значение
# в завистмости вводиться значение пользователем или нет
print("Эльмор: Приветствую вас, путник! Я загадал вам одну загадку.")
user_input: str = input('Введите свой ответ: ')

result: bool = bool(user_input)

print('Эльмор:', result)

# подсмотрел логику решения в теории