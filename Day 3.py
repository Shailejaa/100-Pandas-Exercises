# import random
# check = random.randint(0,1)
# print(check)
#
# random.seed(2)
# print(random.random())
# print(random.random())
#
# state = random.getstate()
# print(random.random())
#
# random.setstate(state)
# print(random.random())


# Write your code below this line 👇
# Hint: Remember to import the random module first. 🎲

# import random
#
# print("Welcome to Random Coin Head/Tail Generator.")
# dec1 = input("Would you like to go ahead and start the game? Type Y/N\n").upper()
# if dec1 == 'Y':
#     ran = random.randint(0, 1)
#     if ran == 1:
#         print('Heads')
#     else:
#         print('Tails')
# elif dec1 == 'N':
#     print("Sure, Please take your time to decide.")
# else:
#     print("You entered invalid code. Please try again with valid inputs.")

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
# result = random.choice(names)
# print(f"{result} is going to buy a meal today.")

num = random.randrange(len(names)-1)
result = names[num]
print(f"{result} is going to buy a meal today.")












