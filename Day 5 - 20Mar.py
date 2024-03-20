# 1. Summ even numbers from 1 o 100:
#Write your code below this row 👇
# sum = 0
# for i in range(2,101,2):
#   sum+= i
# print(sum)
# 2. FizzBuzz interview challenge:
# Write your code below this row 👇
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print('FizzBuzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)


# 3. Password Generator Project:
#
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
#
# #Eazy Level - Order not randomised:
# #e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# l_choice = []
# s_choice = []
# n_choice = []
# for i in range(1,nr_letters+1):
#   final = random.choice(letters)
#   l_choice.append(final)
#
# for i in range(1,nr_symbols+1):
#   finals = random.choice(symbols)
#   s_choice.append(finals)
#
# for i in range(1,nr_numbers+1):
#   finaln = random.choice(numbers)
#   n_choice.append(finaln)
#
# result = l_choice+s_choice+n_choice
# f = ''
# for a in result:
#   result1 = str(a)
#   f += result1
# print(f)
#
# #Hard Level - Order of characters randomised:
# #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
#
# result = l_choice+s_choice+n_choice
# random.shuffle(result)
# fs = ''
# for d in result:
#   g = str(d)
#   fs += g
# print(fs)
#
