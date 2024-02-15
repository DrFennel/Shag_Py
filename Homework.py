# таблица умножения!!! в столбиках

'''
print('Multiplication table')
 
for i in range(1, 11):
    for k in range(1, 6):
        print(f'{k:2}  * {i:2} = {(i * k):3}\t', end = '')
    print('')
print('')
for i in range(1, 11):
    for k in range(6, 11):
        print(f'{k:2}  * {i:2} = {(i * k):3}\t', end = '')
    print('')
'''

# ромбики
'''
space_up = width = int(input('input width: '))

for i in range(0, width):
    for k in range(0, space_up):
        print(end=' ')
    space_up -= 1
    for k in range(0, i + 1):
        print('*', end=' ')
    print('')

for i in range(width -2, -1, -1):
    for k in range(space_up, -2, -1):
        print(end=' ')
    space_up +=1
    for k in range(0, i + 1):
        print('*', end=' ')
    print('')
'''
# проверить то, что каждое слово в строке начинается с заглавной буквы
'''
phrase = input('Input your phrase: ')
symbol = ''

for i in phrase:
    if symbol == ' ':
        if ord(i) > 97 or ord(i) < 123:
            print(i, '- is small letter!')
    symbol = i
'''

##найти индекс первого вхождения подстроки в строку
'''
phrase = input('Input your phrase: ')
piece = input('Input piece: ')
##txt = "Hello world! Goodbye world!"
index = 0
counter = -1
piece_counter = 0
piece_check = ''
piece_len = -1
for i in piece:
    piece_len += 1
for i in phrase:
    counter += 1
    if i == piece[piece_counter]:
        index = counter
        piece_counter += 1
        piece_check = piece_check + i
##        print(piece_counter, 'PC', piece_check, 'PCK', piece_len, 'PL', counter, 'COUNTER')
    else:
        piece_counter = 0
        piece_check = ''
##        print(piece_counter, 'PC', piece_check, 'PCK', piece_len, 'PL', counter, 'COUNTER')
    if piece_check == piece:
        break
print('Index: ', index - piece_len)
##print(piece_counter, 'PC', piece_check, 'PCK', piece_len, 'PL', counter, 'COUNTER')
'''


##подсчитать то, сколько раз определённый символ встречается в строке
'''
phrase = input('Input your phrase: ')
counter = 0

while True:
    letter = input('Input the letter what we are looking for: ')
    if ord(letter) > 64 and ord(letter) < 91:
        big = ord(letter)
        small = ord(letter) + 32
        break
    elif ord(letter) > 96 and ord(letter) < 123:
        small = ord(letter)
        big = ord(letter) - 32
        break
    else:
        print('Warning! Invalid input!')

for i in phrase:
    if ord(i) == small or ord(i) == big:
        counter +=1

print(counter)
'''
##сделать первый символ строки заглавной буквой

'''
phrase = input('Input your phrase: ')

letter = ord(phrase[0]) - 32
print(chr(letter) + phrase[1:])
'''

##вставить содержимое переменной в строку, воспользовавшись методом format()
'''
pet = input('Enter your favorite pet: ')
if pet == 'dog' or pet == 'dogs':
    print(' Oh, {}. Sure, I like dags. I like caravans more.'.format(pet)+ chr(0xA9))
elif pet == 'cat' or pet == 'cats':
    print('Nice, {}!! I like furry demons too!'.format(pet))
else:
    print('Who is {}?'.format(pet))
'''

##узнать о том, что в строке содержатся только цифры

'''
some_str = input('Enter some string: ')
counter = 0

for i in some_str:
    if (ord(i) < 48 or ord(i) > 57) and ord(i) != 0x20:
        print('False! You enter letter!')
        break
    counter += 1
if counter == len(some_str):
    print('Well done')
'''

##разделить строку по заданному символу не используя метод split()

'''
phrase = input('Input your phrase: ')
symbol = input('Input letter: ')
##txt = "hello, my name is Peter, I am 26 years old"
piece = ''

for i in phrase:
    piece += i
    if i == symbol:
        print(piece)
        piece = ''
print(piece)
'''


##проверить строку на то, что она составлена только из строчных букв
'''
some_str = input('Enter some string: ')
counter = 0

for i in some_str:
    if (ord(i) < 97 or ord(i) > 122) and ord(i) != 0x20:
        print('False! You enter big letter or number or symbol!')
        break
    counter += 1
if counter == len(some_str):
    print('Well done')
'''
##«перевернуть» строку ("hello world" 'dlrow olleh')
'''
phrase = input('Input your phrase: ')

for i in phrase[::-1]:
    print(i, end = '')
'''
