# name= int(input())
# last_name= int(input()) 
# age= int(input()) 
# city= int(input()) 
# print(f'Вас зовут {name} {last_name}, Ваш возрост: {age}, Вы проживаете в городе {city}')




# name = input() 
# last_name = input() 
# age = int(input()) 
# city = input() 
# print(f'Вас зовут {name} {last_name}, Ваш возраст: {age}, Вы проживаете в городе {city}')




# str1 = 'birthday'
# print(str1[5:])
# print(str1[:5])



# string = 'Kolobok poshel v les i propal'
# print(string[1::2])



# string = 'abracadabra'
# result = string.replace('c', 'k')
# print(result)




# string = 'abracadabra' 
# s1 = string[:5] + "K" + string[6:] 
# print(s1)



# string = 'I love Python' 
# string1 = string.startswith('Python') 
# print(string1)





# string1 = "America" 
# string2 = "Japan" 
# print(string1[:1] + string2[:1] + string1[int(len(string1)/2)] + string2[int(len(string2)/2)] + string1[-1] + string2[-1])






# a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
# for k,v in a.items():
#     a[k] = v / 5

# print(a)






# a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
# for k,v in a.items():
#     a[k] = v / 5

# print(a)



# a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
# for k,v in a.items():
#     a[k] = v / 5

# print(a)



# a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
# for k,v in a.items():
#     a[k] = v / 5

# print(a)






# a = int(input()) 
# b = int(input()) 
# c = int(input()) 
# if a <= b and a <= c and b <= c: 
#     print(a,b,c) 
# elif a <= c and a <= b and c <= b: 
#         print(a,c,b) 
# elif b <= a and b <= c and a <= c: 
#         print(b,a,c) 
# elif b <= c and b <= a and c <= a: 
#     print(b,c,a) 
# elif c <= a and c <= b and a <= b: 
#     print(c,a,b) 
# elif c <= b and c <= a and b <= a: 
#     print(c,b,a) 
# else: 
#     print(a,b,c)





# a = int(input()) 
# b = int(input()) 
# c = int(input()) 
# if a <= b and a <= c and b <= c: 
#     print(a,b,c) 
# elif a <= c and a <= b and c <= b: 
#         print(a,c,b) 
# elif b <= a and b <= c and a <= c: 
#         print(b,a,c) 
# elif b <= c and b <= a and c <= a: 
#     print(b,c,a) 
# elif c <= a and c <= b and a = b: 
#     print(c,a,b) 
# else: 
#     print(c,b,a)








# num = int(input())
# if num = 9 and num <= 11:
#     print("осень")
# elif num == 12 or num == 1 or num == 2:
#     print("зима")
# elif num >= 3 and num <= 5:
#     print("весна")
# elif num >= 6 and num <= 8:
#     print("лето")
# else:
#     print("Такого месяца нет") 



# string = input()
# if string.isdigit():
#     print("is digit")
# elif string.isalpha():
#     print("is alpha")
# else:
#     print("is ASCII")

# не верный вариант

# p = int(input())
# r = int(input())
# z = int(input())
# if p <= r and p <= z or r <= p and r <= z or z <= p and z <= r:
#     print('yes')
# else:
#     print('no')


# правельный вариант

# p = int(input())
# r = int(input())
# z = int(input())
# if p + r > z and r + z > p and p + z > r:
#     print('yes')
# else:
#     print('no')



# a1, b1, c1 = int(input()), int(input()), int(input()) 
# # c = max(a1, b1, c1) 
# # b = min(a1, b1, c1) 
# # a = sum([a1, b1, c1]) - min(a1, b1, c1) - max(a1, b1, c1) 
# if c >= a + b: 
#     print('impossible') 
# elif c**2 == a**2 + b**2: 
#     print('rectangular') 
# elif c**2 < a**2 + b**2: 
#     print('acute') 
# elif c**2 > a**2 + b**2: 
#     print('obtuse')