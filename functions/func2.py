# def reverse(string):
#     
#     str2 = str1.split(' ')
#     str3 = str2[::-1]
#     str4 = ' '.join(str3)
#     return str4
# print(reverse('Hello world! My name is John, Last name is Snow. Nice to meet you!'))

# str1 = 'Hello world! My name is John, Last name is Snow. Nice to meet you!'

# def get_reversed_string(text):
#     # print(text[::-1])
#     spisok = text.split()[::-1]
#     # print(spisok[::-1])
#     return ' '.join(spisok)

# print(get_reversed_string(str1))
# print(get_reversed_string('Kolobok повесился а пряник плачет'))

# def sum_of_args(a,b,c=5,d=5): # параметры
#     return a + b + c + d

# result = sum_of_args(1,2,3,4) # АРГУМЕНТЫ
# print(result)
# res = sum_of_args
# # print(res, type(res))
# print(res(5,6,7,8))
# print(sum_of_args(5,5))


###############################################

# позиционные и именованные аргументы

# def printParms(a,b,c):
#     print(a, 'is stored in parm a')
#     print(b, 'is stored in parm b')
#     print(c, 'is stored in parm c')
    
# printParms(5, 10, 15)
# print()
# printParms(c=5, b=15, a=10)
# print()
# printParms(a=20, b=30, c=15)


# def sum_of_args(a,b,c=5,d=5): # параметры
#     return a + b + c + d

# print(sum_of_args(5, 10, 15, 20)) # arguments(позиционные пргументы)
# print(sum_of_args(a=5, c=20, b=10, d=15)) # keyword arguments (именованные аргументы)
# print(sum_of_args(5, 10, d=15, c=20))

#################################################
# оператор *
# a = [1,2,3]
# b = [4,5,6]
# c = [*a, *b]
# d = a + b
# print(c)
# print(d)

#################################################
# *args, **kwargs в функциях

# def printScores(student, *args):
#     print(f'Name of student:{student}')
#     # print(args)
#     print(f'AVG: {sum(args) / len(args)}')
#     for x in args:
#         print('Score:', x)
# printScores('John Snow', 100,90,80,95,88)


# def printPetnames(owner, **pets): #{'key': 'value'}
#     print(f'Owner name: {owner}')
#     # print(pets)
#     for pet, name in pets.items():
#         if type(name) == list:
#             print(f'{pet}:', *name)
#         else:

#             print(f'{pet}: {name}')
# printPetnames('John Snow', dog='Pluto', cat='Garfild', fish=['Nemo', 'Dori','Batya'], turtle='Leonardo')

# def get_some_date(a,b, *args, **kwargs):
#     print('параметры a и b:', a, b)
#     print('аргументы:', [*args])
#     print('именованные аргументы', kwargs)

# get_some_date(1,2,3,4,5, lang='Python', car='BMW')


##################################################################
## ГЕНЕРАТОР ПАРОЛЕЙ

# def generate_random_string(len_):
#     import string as s
#     import random
#     # print(s.ascii_letters, s.digits, s.punctuation)
#     symbols = s.ascii_letters + s.digits
#     res = list(
#         random.choice(symbols) for i in range(1, len_)
#     ) + list(random.choice(s.punctuation))
#     # print(s.punctuation)
#     random.shuffle(res)

#     return ''.join(res)
    

# print(generate_random_string(15))
# print(generate_random_string(44))
# print(generate_random_string(33))
# print(generate_random_string(16))
# print(generate_random_string(11))






















