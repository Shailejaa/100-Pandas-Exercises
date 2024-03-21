# Hurdle 1:
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def hurdle():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
# while at_goal() == False:
#     hurdle()
#     if at_goal() == True:
#         done()

# 2. hurdle 2: Same code as hurdle 1:
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def hurdle():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
# while at_goal() == False:
#     hurdle()
#     if at_goal() == True:
#         done()


# Hurdle 3:
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def hurdle():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
# while at_goal() == False:
#     while wall_in_front():
#         hurdle()
#         if at_goal() == True:
#             done()
#     while front_is_clear():
#         move()

# same problem with different solution like if in while loop
# while at_goal() == False:
#     if wall_in_front():
#         hurdle()
#         if at_goal() == True:
#             done()
#     elif front_is_clear():
#         move()

# Hurdle 4:
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def hurdle():
#     turn_left()
#     while front_is_clear():
#         move()
#         if at_goal():
#             done()
#         elif right_is_clear():
#             turn_right()
#
# while at_goal() == False:
#     if front_is_clear():
#         move()
#     elif wall_in_front():
#         hurdle()

# Maze:
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# while front_is_clear():
#     move()
# turn_left()
# while at_goal()== False:
#     if right_is_clear():
#         turn_right()
#         if front_is_clear():
#             move()
#         else:
#             turn_left()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()

