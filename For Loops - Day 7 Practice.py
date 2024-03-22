# 1. Print the first 10 natural numbers using for loop.

# for i in range(1,11):
#     print(i)
#
# natural_numbers = [x for x in range(1,11)]
# print(natural_numbers)

# 2. Python program to print all the even numbers within the given range.

# start_number = int(input('Enter start number: \n'))
# end_number = int(input('Enter end number: \n'))
#
# for num in range(start_number, end_number+1):
#     if num % 2 == 0:
#         print(num)
#
# even = [x for x in range(start_number, end_number+1) if x % 2 == 0]
# print(even)

# 3. Python program to print all the table output within the given number.

# number = int(input("Enter the number of which you want to view Table: \n"))
#
# for num in range(number, ((number*10)+1)):
#     if num % number == 0:
#         print(num)
#
# table = [x for x in range(number, ((number*10)+1)) if x % number == 0]
# print(table)

# 4. Python program to calculate the sum of all numbers from 1 to a given number.

# end = int(input("Enter the number where you want to end: \n"))
#
# sum2 = 0
# for num in range(1, end+1):
#     sum2 += num
# print(sum2)
#
# # OR
# sum1 = 0
# sum_output = [sum1 := sum1 + x for x in range(1, end+1)]
# print(sum_output[-1])
#
# # OR
# sum_output2 = sum(x for x in range(1, end+1))
# print(sum_output2)

# 5. Python program to calculate the sum of all the odd numbers within the given range.
# sum1 = 0
# for num in range(1, end+1):
#     if num % 2 != 0:
#         sum1 += num
# print(sum1)
#
# # OR
# sum2 = 0
# output = [sum2 := sum2 + x for x in range(1,end+1) if x % 2 != 0 ]
# print(output[-1])
#
# # OR
# sum3 = 0
# output2 = sum(x for x in range(1, end+1) if x % 2 != 0)
# print(output2)

# 6. Python program to display output from a list using a for loop.

# numbers_list = input("Input: \n")
# numbers_list = list(numbers_list)
# print(numbers_list)
#
# for i in numbers_list:
#     print(i)

# 7. Python program to count the total number of digits in a number.

# inp = [1,2,3,4,5,6,7,5,3,6,3,8,9,4,2,3,6,8,4,3,7,8,9,4,3,7,52,6,8,5]
# counter = 0
# for num in inp:
#     counter += 1
# print(counter)
#
# # OR
# counter1 = 0
# output = [counter1 := counter1 + 1 for x in inp]
# print(output[-1])

# 8. Python program to check if the given string is a palindrome.

# word = input("Enter a word here: \n").lower()
# word1 = list(word)
# print(word1)
# word1.reverse()
# reversel = word1
# # print(reversel)
# if reversel == list(word):
#     print(f"Yes, the word {word} is Palindrome.")
# else:
#     print(f"No, the word {word} is Not Palindrome.")

# 9. Python program to print all the prime numbers within the given range.

# end = int(input("Enter the range: \n"))
#
# for num in range(1, end+1):
#     if num > 1:
#         for i in range(2, num): # not added num + 1 because because anyway if a num gets divisible by 2 or any number before num then the condition as statement will break first and will not continue.
#             if num%i == 0:
#                 break
#         else:
#             print(num)

