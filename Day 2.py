# 1. Roller Coaster Ticket with Multiple if statements:

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
#
# if height >= 120:
#     age = int(input("What is your age? "))
#     if age < 12:
#         photo = input("Do you want to photograph the ride? y/n ")
#         if photo == 'y':
#             print("The total bill is 8$.")
#         else:
#             print("The cost of ride is 5$.")
#     elif age <= 18:
#         photo = input("Do you want to photograph the ride? y/n ")
#         if photo == 'y':
#             print("The total bill is 10$.")
#         else:
#             print("The cost of ride is 7$.")
#     else:
#         photo = input("Do you want to photograph the ride? y/n ")
#         if photo == 'y':
#             print("The total bill is 15$.")
#         else:
#             print("The cost of ride is 12$.")
# else:
#     print("Sorry you can't ride the roller coaster now.")


# 2. Pizza Price calculator
#
# # 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# # 🚨 Don't change the code above 👆
#
# # Write your code below this line 👇
# small_pizza_bill = 15
# medium_pizza_bill = 20
# large_pizza_bill = 25
# pep_s = 2
# pep_m_l = 3
# ext_cheese = 1
#
# size = size.upper()
# add_pepperoni = add_pepperoni.upper()
# extra_cheese = extra_cheese.upper()
#
# bill = 0
# if size == 'S':
#     bill += small_pizza_bill
# elif size == 'M':
#     bill += medium_pizza_bill
# elif size == 'L':
#     bill += large_pizza_bill
# else:
#     print("Invalid Entry.")
#
# if add_pepperoni == 'Y':
#     if size == 'S':
#         bill += pep_s
#     elif size == 'M' or size == 'L':
#         bill += pep_m_l
# else:
#     print('Invalid Entry. Please Enter Valid option from Y/N.')
#
# if extra_cheese == 'Y':
#     bill += ext_cheese
#
# print(f'The final bill amounted to {bill}$.')
#
#
# # 3. Love Calculator
# # 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# # 🚨 Don't change the code above 👆
#
# # Write your code below this line 👇
# name1 = name1.lower()
# name2 = name2.lower()
# count = 0
# check1 = 'true'
# check2 = 'love'
# truefinal = []
# for name in check1:
#     for i in name1:
#         if name == i:
#             count += 1
#     for l in name2:
#         if name == l:
#             count += 1
# if count:
#     truefinal.append(count)
#
# count2 = 0
# lovefinal = []
# for name in check2:
#     for i in name1:
#         if name == i:
#             count2 += 1
#     for l in name2:
#         if name == l:
#             count2 += 1
# if count2:
#     lovefinal.append(count2)
#
# finaltrue = truefinal.pop()
# finallove = lovefinal.pop()
#
# final = str(finaltrue) + '' + str(finallove)
# final = int(final)
#
# if final < 10 or final > 90:
#     print(f'Your score is {final}, you go together like coke and mentos.')
# elif final >= 40 and final <= 50:
#     print(f'Your score is {final}, you are alright together.')
# else:
#     print(f'Your score is {final}.')


