# sentence = input('Vvedite predlojeniye: ')
# # if sentence[-1] == '?':
# #     print('Yes, vopsotel\'noye!')
# # else:
# #     print('No, normal\'one')

# print('Yes vopsote\'noye!: ' if sentence[-1] == '?' else 'No, normal one!') 


#_________________________________________________________________
 
# Ternary operators(Тернарный оператор)- это конструкция которая по своему действию аналогична конструкции if/else,
# но при этом записывается в одну строку

# number = int(input('Vvedite chislo:'))
# res = 'even number' if number % 2 == 0 else 'odd number'
#          # чётное                             # нечётное
# print(res)



# <выражение если True> if <условие> else <выражение если False>

# ls = [55,65,75,89,100,15,6]
# print(ls)
# choice = input('Vvedite max/min:')
# res = max(ls) if choice.lower().strip() == 'max' else min(ls)
# print(res)
# if choice.lower().strip() == 'max':
#     print(max(ls))
# elif choice.lower().strip() == 'min':
#     print(min(ls))
# else:
#     print('Invalid chice!')


# res = max(ls) if choice.lower().strip() == 'max' else min(ls) if choice.lower().strip() == 'min' else 'Invalid choise!'
# print(res)

#_______________________________________

# flag = True
# symbols = '0123456789' + '-' + '.'

# while flag:
#     print()
#     num1 = input('Введите первое число:')
#     is_correct_number = True
#     for x in num1:
#         if x not in symbols:
#             print('Вы ввели не правельное число!')
#             is_correct_number = False
#             break

#     if not is_correct_number:
#         continue
        

#     num2 = input('Введите второе число:') 
#     for x in num2:
#         if x not in symbols:
#             print('Вы ввели не правельное число!')
#             is_correct_number = False
#             break
#     if not is_correct_number:
#         continue


#     num1 = float(num1) if '.' in num1 else int(num1)
#     num2 = float(num2) if '.' in num2 else int(num2)


#     # print(num1, type(num1))
#     # print(num2, type(num2))

#     operator = input('Введите операторы(+, -, *, /):').strip()


#     if operator == '+':
#         print(f'Результат: {num1 + num2}')
#     elif operator == '-':
#         print(f'Результат: {num1 - num2}')
#     elif operator == '*':
#         print(f'Результат: {num1 * num2}')
#     elif operator == '/':
#         if num2 == 0:
#             print('На ноль делить нельзя!!')
#         else:
#             print(f'Результат: {num1 / num2}')
#     else:
#         print('Вы ввели не верный оператор!!!')

#     choice = input('Хотите продолжить(y/n)?')
#     if choice.lower().strip() != 'y':
#         flag = False
#         print('Пока пока!!')










string = '123321'

if int(string[0]) + int(string[1]) + int(string[2]) == int(string[3]) + int(string[4]) + int(string[5]) + int(string[6]):
    print('Да')
else:
    print('Нет')




prin





































































































