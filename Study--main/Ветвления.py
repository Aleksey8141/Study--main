'''
Написать программу, которая будет конвертировать значение температуры
из градусов Цельсия в Фаренгейты и наоборот.
Входные данные: 60С, 45F, ... .
Результат:
Расчетніе формулы:

с = (F-32) * 5/9
F = C * 9/5 + 32

----------------
Тестовые значения:
60С     140F
90C     194F
100C    212F

45F     7.22C
90F     32.22C
125F    52.67C
50a     Wrong value

'''

t = '90c'

suffix = t[-1]
val = int(t[:-1])

if suffix in ['C', 'c']:
    conv_val = val*9/5+32
    result = str (conv_val) + 'F'
elif suffix in ['F', 'f']:
    conv_val = (val-32)*5/9
    result = str(conv_val) + 'F'
else:
    result = 'Wrong value'
print(t, 'is', result)