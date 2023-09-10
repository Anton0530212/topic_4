# Программа, которая принимает положительное трехзначное число
# и рассчитывает сумму и произведение его цифр.
number: int = int(input('Введите положительное трехзначное число: '))

hundreds: int = number // 100
tens: int = number // 10 % 10
units: int = number % 10

sum_digit = hundreds + tens + units
product_digits = hundreds * tens * units

print('Сумма цифр:', sum_digit)
print('Произведение цифр:', product_digits)
