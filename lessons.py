'''
for i in range(1, 11):
    for k in range(1, 6):
        print(k, '*', i, '=',(i * k),'\t', end = '')
    print('')
print('')
for i in range(1, 11):
    for k in range(6, 11):
        print(k, '*',i, '=', (i * k),'\t', end = '')
    print('')
'''
'''
n = 11
if n % 2 == 0:
    n -= 1

for i in  range(n,-1,-2):
    print(i)

for i in range(n):
    print(i)
'''

'''
str_val = 'Hi Python'

for i in str_val:
    print(i, end='*')
'''

'''
a = 173
d = 28
'''
'''
str_val = 'ехал грека через реку'

for i in str_val:
    if i == 'р':
        print('*', end='')   
    else:
        print(i,end='')
'''

'''
name = 'Vasia'
name2 = 'Vasia'
print(name is name2)
'''
'''
str_var = 'string'
##str_var[3] = '3'
print(str_var[:3])
'''

# счетчик строки

''''
str_val = input('Input same phrase: ')
counter = 0
for i in str_val:
    if i == ' ':
        continue
    counter +=1

print('There are', counter, 'symbols without " " in your phrase.')

'''

'''
min_num = int(input('Input min number: '))
max_num = int(input('Input max number: '))
choise = input('Choise even(2) or odd(1)')


if choise == '2':
    if min_num % 2 != 0:
        min_num += 1
else:
    if min_num % 2 != 1:
        min_num += 1

for i in range(min_num, max_num+1, 2):
    print(i)
'''

# СТРОКИ 7 FEB
'''
val = r
print(val)

val.
'''

'''
name = 'vasia'
name2 = 'vasia'
print(id(name), ' ', id(name2))
name2 = name + name2
print(id(name), ' ', id(name2))
'''

'''
stroka = 'mama myla ramy'
print(stroka.find('l', 3))
'''
'''
stroka = 'mama\n myla ramy'
print(stroka)
print(hash('mama'))
'''

'''
split join

dog string \n 
'''

'''
str_val = 'string'
s_list = [1,2,4]
print(id(s_list))
copy_list = s_list
a_list = [5,9.8]
s_list.extend(str_val)

print(s_list)
s_list.pop()

print(s_list, copy_list)

print(*s_list)

s_list.copy


coppy_list = s_list.copy()
print(coppy_list)

s_list[0] = 99
print(s_list, coppy_list)
'''

'''
sam_str = 'hello world'
new = sam_str[-1::-1]
print(new)
'''

# same_list = []

# for i in range(10):
#    same_list.append(i)

# same_str = 'string'

# same_list = [i for i in same_str]

# print(same_list)

# print([i for i in 'string'])

# print([i for i in range(20) if i % 2 == 0 ])


# def greeting(name,hi,time):
#    print(f'{hi} {name} {time}')
# greeting('1200','Vasya', hi ='hello')

# def greeting(name = 'user', hi = 'Hello'):
#    print(f'{hi} {name}')
# greeting(name='Vasya',hi='kek')

'''
def greeting(name,time):
    if time in range(5,12):
        daypart = 'morning'
    elif time in range(12,18):
        daypart = 'day'
    elif time in range(18,23):
        daypart = 'evening'
    elif time in range(0,25):
        daypart = 'night'
    else:
        return print('you are stupid')
    print(f'Good {daypart}, {name}')
'''
'''
import mymodule

mymodule.greeting()
'''

######28.02
'''
def bmi(mass,hight):
        bmi_val = mass / (hight * 2)
        result = 'your OK'
        if bmi_val > 29.9:
            result = 'you fat'
        elif bmi_val < 18.5:
            result = 'low mass'
        return f'your bmi = {round(bmi_val,1)} {result}'



mass = float(input('input mass: '))
hight = float(input('input hight: ')) / 100

print(bmi(mass,hight))
'''

# # ####доделать !!!!!!!!!!!!!!
# user_id = input('user:')
# pwd = input('pwd:')
#
# def greeting(user_id,pwd):
#     str_val = 'Guest'
#     user_id = user_id.lower()
#     if user_id == 'admin':
#         str_val = 'Admin'
#     elif user_id == 'user':
#         str_val = 'User'
#     return f'Hello {str_val}, {user_id.capitalize()}'
#
#
# print(greeting(user_id,pwd))


# def averege_arif(*args):
#     sum_num = 0
#     counter = 0
#     for i in args:
#         sum_num += int(i)
#         counter += 1
#     return sum_num / counter
# # print(averege_arif(99, 71, 53, 7, 101))
# averge_mark = averege_arif
# print(type(averege_arif))
# print(averge_mark(7,4,2,6,7))

# users = [['user_n1', 111],['user_n2',333],['user_3',222]]
# def accaunt()

# доделать 2 функции.
# customers = ['AdminFedya','AdminVasya','guest', 'student_09']
# def say_hell(castomer):
#     if castomer.find('admin') != -1:
#         return 'Hello Admin'
#     if castomer.find('')


# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result
#
# print("\n\nRecursion Example Results")
# tri_recursion(6)

#######################

# def my_greeting1():
#     print('Hello! Have a good morning!')
#
# say_good_morning = my_greeting1
#
# say_good_morning()
#
# def my_greeting2():
#     print('Hello! Have a good day!')
#
# def my_greeting3():
#     print('Hello! Have a good evening!')
# def my_greeting4():
#     print('Hello! Have a good night!')
#
# my_greeting_list = [my_greeting1, my_greeting2, my_greeting3, my_greeting4]
#
# for my_greenting in my_greeting_list:
#     my_greenting()
#
# def greeting_recipient(greeting_fune):
#     greeting_recip = input('Input your name: ')
#     print('Deer,', greeting_recip, '!')
#     greeting_fune()
#
# for my_greenting in my_greeting_list:
#     greeting_recipient(my_greenting)
#
# def check_time_day():
#     while True:
#         timeOfDay = input("Input time of day (M-morning;D-afternoon;E- everning;N-night):")
#         if timeOfDay == "M":
#              return my_greeting_list[0]
#         elif timeOfDay == "D":
#              return my_greeting_list[1]
#         elif timeOfDay == "E":
#             return my_greeting_list[2]
#         elif timeOfDay == "N":
#             return my_greeting_list[3]
#         else:
#             print("Wrong input!")

