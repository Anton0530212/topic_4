# Программа, которая принимает положительное трехзначное число
# и рассчитывает сумму и произведение его цифр.
number: int = int(input('Введите положительное трехзначное число: '))

hundreds: int = number % 10
tens: int = number // 10 % 10
units: int = number // 100 % 10

sum_digit = hundreds + tens + units

product_digits = hundreds * tens * units

print('Сумма цифр:', sum_digit)
print('Произведение цифр:', product_digits)

# Очень долго решал, не мог понять как разделить число на цифры
# делал так hundreds = number[0]
# но индексы не мог потом сложить или умножить так как это строки