'''
Дана строка и нужно найти ее первое слово.

Строка состоит только из английских символов и пробелов.
В начале и в конце строки пробелов нет.
'''
def first_word(text):
    text = 'greeting from CheckiO Planet'
    text = text.split(' ')
    # del text[1::] you can take first element instead deleting other
    return text[0]
first_word('')
print(first_word(''))

assert first_word('Hello world') == 'Hello'
assert first_word('a word') == 'a'
assert first_word('greeting from CheckiO Planet') == 'greeting'
assert first_word('hi') == 'hi'

#def first_word(text):
#    text = 'Hello world'
#    text = text.split(' ')[0]
#    #del text[1::]
#    return text
#first_word('')
#print(first_word(''))

#assert first_word('Hello world') == 'Hello'
#assert first_word('a word') == 'a'
#assert first_word('greeting from CheckiO Planet') == 'greeting'
#assert first_word('hi') == 'hi'
