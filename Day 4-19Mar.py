# # Rock Paper Scissor game:
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
#
# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''
#
# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
#
# # Write your code below this line 👇
# import random
#
# choice = int(input("What do you choose?Type 0 for Rock, 1 for Paper and 2 for Scissors."))
#
# computer_choice = [0, 1, 2]
# computer_choice = random.choice(computer_choice)
# if choice <= 2 and choice >= 0:
#     if choice == 0:
#         print(f'Your Choice is Rock. \n{rock}')
#     elif choice == 1:
#         print(f'Your Choice is Paper. \n{paper}')
#     elif choice == 2:
#         print(f'Your Choice is Scissor. \n{scissors}')
#
#     if computer_choice == 0:
#         print(f'Computer\'s Choice is Rock. \n{rock}')
#     elif computer_choice == 1:
#         print(f'Computer\'s Choice is Paper. \n{paper}')
#     elif computer_choice == 2:
#         print(f'Computer\'s Choice is Scissor. \n{scissors}')
#
#     if choice == 0 and computer_choice == 2:
#         print('You Win.')
#     elif choice == 1 and computer_choice == 0:
#         print('You Win.')
#     elif choice == 2 and computer_choice == 1:
#         print('You Win.')
#     elif choice == computer_choice:
#         print('Tie.')
#     else:
#         print('You Lose.')
# else:
#     print('Please Enter Valid Entry.')


#2. Treasure MAP game:
#
# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
#
# position = input("Where do you want to put the treasure? ")
#
# horizontal = int(position[0])
# vertical = int(position[1])
#
# map[vertical - 1][horizontal - 1] = "X"
#
# print(f"{row1}\n{row2}\n{row3}")

# 3. Calculate avg heights of students:
#
# # 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆
#
#
# #Write your code below this row 👇
# counter = 0
# for i in student_heights:
#   counter+=1
#
# sum = 0
# for s in student_heights:
#   sum+=s
#
# result = round((sum/counter))
# print(f'Average Heights of Students is {result}.')
#

# 4. Calculate highest score:
# 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 🚨 Don't change the code above 👆
#
# # Write your code below this row 👇
# high = 0
# for i in student_scores:
#     if i > high:
#         high = i
#
# print(high)


# Carl Gauss's adding 1 to 100 logic:
# sum = 0
# for i in range(1,101):
#     print(i)
#     sum += i
#     print(sum)