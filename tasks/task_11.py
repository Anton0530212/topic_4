# Программа, которая принимает четырехзначное число и
# выводит его цифры на отдельных строках
number: int = int(input('Введите четырехзначное число: '))

thousands: int = number // 1000
hundreds: int = number // 100 % 10
tens: int = number // 10 % 10
units: int = number % 10

print('Цифра в позиции тысяч:', thousands)
print('Цифра в позиции сотен:', hundreds)
print('Цифра в позиции десятков:', tens)
print('Цифра в позиции единиц:', units)
