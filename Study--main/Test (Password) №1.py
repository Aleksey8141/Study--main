'''
Напишите программу, которая позволит выполнять проверку пароля на сложность
в соответствии со следующими критериями:
* длина пароля не менее 5 символов
* содержит буквы латинского алфавита как в верхнем, так и в нижнем регистре: A-Z, a-z
* содержит цифры от 0 до 9
* содержит хотя бы один из символов: @, #, %, &
'''

password = 'Akot@'

cond1 = len(password) >= 5
cond2 = not password.islower() and not password.isupper()
cond3 = len({'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'} & set(password)) > 0  # перевел числа в строку
cond4 = len({'@', '#', '%', '&'} & set(password)) > 0
if cond1 and cond2 and cond3:
    print('Password is difficult enough')
else:
    print('Password is not difficult enough')
