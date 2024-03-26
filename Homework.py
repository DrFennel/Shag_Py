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

# def greeting(name,hi,time):   5-12 12-18 18-23 23-5


##                  Найти индексы всех вхождений в список.


##s_list = [2,3,99,99,85,7,2,3,6,7,1,6,8,7,3,2,1,6,78,9,23,1,6,2,5,12,4,2,0,0,5,7,1,0,2,3,5,4,2,1,2,5,4,7,1]
##some_val = int(input('Enter num: '))
##index = -1
##ind_list = []
##
##while some_val in s_list[index + 1:]:
##    index = s_list.index(some_val,index + 1)
##    ind_list.append(index)
##    
##print(ind_list)
##


# таблица умножения!!! в столбиках через вложеные списки в одну строку!!!


# print('Multiplication table')
#
# for i in range(1, 11):
#     for k in range(1, 6):
#         print(f'{k:2}  * {i:2} = {(i * k):3}\t', end = '')
#     print('')
# print('')
# for i in range(1, 11):
#     for k in range(6, 11):
#         print(f'{k:2}  * {i:2} = {(i * k):3}\t', end = '')
#     print('')
#################################
# user_list = [['user_n1', 111], ['user_n2', 333], ['user_3', 222]]
#
#
# def accaunts(users, act = 0):
#     ''' default print "Username = user, Password = pwd".
#      If 2nd argument = 1 return tuple in format [Username = user, Password = pwd,]'''
#     acc_list = []
#     for i in users:
#         acc_list.append('Username = {0}, Password = {1}'.format(i[0],i[1]))
#     if act == 1:
#         return acc_list
#     elif act == 0:
#         print(*acc_list)
#
#
# # def accaunts(users):
# #     for i in users:
# #         print('User = ', i[0], 'Password = ', i[1])
#
# help(accaunts)
# list = accaunts(user_list,1)
# print(*list)
#################################

# users = [['Pin',123],['Bin',456],['Guin',789]]
#
# def data (*args):
#     data_list=[]
#     for i in args:
#         data_list.append (f'user: {i[0]},password: {i[1]}\n')
#     return data_list
#
# print(*data(*users))


#################################
# def fact(num):
#     print(num)
#     if num == 0:
#         return 1
#     return num * fact(num - 1)
#
# print(fact(7))

####################################
# user_word = input('input word: ')
# len_user_word = len(user_word)
#
# def palindrome(word):
#
#
#
# palindrome(user_word)
######################################

# students_name_list = []
# marks_list = []
# personal_mark_list = []
# def input_data():
#     while (last_name := input("Enter the student's last name or enter 0 to exit: ")) != 0:
#         students_name_list.append(last_name)
#         personal_mark_list = input("Enter the student's grades separated by a space: ")
#         marks_list.append(list(map(int, personal_mark_list.split())))
#
# def average_rating():

students_name_list = []
marks_list = []
personal_mark_list = []
averege_list = []
pass_cond_students_list = []
#
# while (last_name := input("Enter the student's last name or enter 0 to exit: ")) != '0':
#      students_name_list.append(last_name)
#      personal_mark_list = input("Enter the student's grades separated by a space: ")
#      marks_list.append(list(map(float, personal_mark_list.split())))
# print(students_name_list)
# print(marks_list)
# for i in marks_list:
#      for k in i:
#           mark_sum, counter = 0, 0
#           mark_sum += k
#           counter += 1
#      averege_list.append(round((mark_sum/counter), 1))
# print(averege_list)
# counter = 0
# for i in averege_list:
#      counter += 1
#      if i > 59.9:
#           pass_cond_students_list.append(f'{students_name_list[counter]} : {i}\n')
#
# print(*pass_cond_students_list)

def data_input():
     while (last_name := input("Enter the student's last name or enter 0 to exit: ")) != '0':
          students_name_list.append(last_name)
          personal_mark_list = input("Enter the student's grades separated by a space: ")
          marks_list.append(list(map(float, personal_mark_list.split())))
def averege(number_list):
     mark_sum, counter = 0, 0
     for i in number_list:
          for k in i:
               mark_sum += k
               counter += 1
          averege_list.append(round((mark_sum/counter), 1))
     print(averege_list)
def pass_cond_stud():
     counter = 0
     for i in averege_list:
          counter += 1
          if i > 59.9:
               pass_cond_students_list.append(f'{students_name_list[counter]} : {i}\n')


marks_list = [[90.0, 66.0, 60.0, 59.9, 0], [90.0, 66.0, 60.0, 59.9, 1], [90.0, 66.0, 60.0, 59.9, 50.0]]
# data_input()
averege(marks_list)
# pass_cond_stud()
# print(*pass_cond_students_list)