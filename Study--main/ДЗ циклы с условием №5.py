'''
Найдите сумму чисел в следующей последовательности: 2,22,222,2222, ..., 2(n),-где n-количество разрядов
в последнем числе. Например, при n=5 последнее число будет 22222, а сумма чисел в последовательности 24690.
'''
import math

n = eval(input('Введите число :'))

i = 1
res = 0
while i <= n:
    res += int('2' * i)
    i += 1
print(res)

