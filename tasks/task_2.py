# Программа, которая принимает два числа a и b и меняет их значения местами
a: int = int(input('Введите число a: '))
b: int = int(input('Введите число b: '))

# a, b = b, a
#
# print("Значения после перестановки:")
# print('a = ' + str(a), 'b = ' + str(b), sep='\n')


temp = a
a = b
b = temp

print("Значения после перестановки:")
print('a = ' + str(a), 'b = ' + str(b), sep='\n')

# Второе решение тоже верно