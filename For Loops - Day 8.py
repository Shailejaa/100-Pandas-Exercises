# 10. Find the factorial of a given number.

# number = int(input('Give the number: \n'))
# output = 1
# for num in range(1, number+1):
#     output *= num
#
# print(output)

# 11. Print all the prime numbers within a given range.

number = int(input('Give the number: \n'))
for num in range(1, number+1):
    if num>1:
        for num1 in range(2, num):
            if num%num1 ==0:
                break
        else:
            print(num)




