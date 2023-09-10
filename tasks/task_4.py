# Задача на последовательность преоритета выполнения операций
num_chicken: int = int(input('Введите количество курочек: '))
num_cows: int = int(input('Введите количество коровок: '))
num_pigs: int = int(input('Введите количество свинок: '))

total_legs: int = num_chicken * 2 + (num_cows + num_pigs) * 4

print('Общее количество ног на ферме:', total_legs)
