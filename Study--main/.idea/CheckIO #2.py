def first_word(text):
    text = 'greeting from CheckiO Planet'
    text = text.split(' ')
    del text[1::]
    return text
first_word('')
print(first_word(''))

assert first_word('Hello world') == 'Hello'
assert first_word('a word') == 'a'
assert first_word('greeting from CheckiO Planet') == 'greeting'
assert first_word('hi') == 'hi'
