# Below works only in Reboorgs World Webpage:
# 1. Draw square:
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# turn_left()
# move()
# turn_right()
# move()
# turn_right()
# move()
# turn_right()
# move()

# 2. Home1:
# move()
# move()

# 3. Home3:
# move()
# move()
# turn_left()
# move()

# 4. Home4:
# def move3():
#     move()
#     move()
#     move()
#
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def direction():
#     turn_left()
#     move3()
#     turn_right()
#     move()
#     turn_right()
#     move3()
#
# move3()
# direction()
# direction()
# direction()
# turn_left()
# move3()

# 5. Around 1:
# def move9():
#     move()
#     move()
#     move()
#     move()
#     move()
#     move()
#     move()
#     move()
#     move()
#
# move9()
# turn_left()
# move9()
# turn_left()
# move9()
# turn_left()
# move9()

# 6. Around 1- Variable:
# put()
# while front_is_clear():
#     move()
#     if wall_in_front():
#         turn_left()
#     elif object_here():
#         done()

# 7. Around 1- Apple:
# while front_is_clear():
#     move()
#     if object_here() and wall_in_front():
#         take()
#         turn_left()
#     elif object_here():
#         take()
#     elif wall_in_front():
#         turn_left()
#     if at_goal():
#         done()

# 8. Around 1:
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# put()
# while front_is_clear():
#     move()
#     if right_is_clear():
#         turn_right()
#     elif wall_in_front():
#         turn_left()
#     if object_here():
#         done()

# Around 3 (toughest):
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def keep_moving():
#     while front_is_clear():
#         move()
#         if object_here():
#             done()
#         if wall_in_front():
#             turn_left()
#             move()
#
#         while right_is_clear():
#             turn_right()
#             move()
#             if wall_in_front():
#                 turn_left()
#                 move()
#
# put()
# if wall_in_front():
#     turn_left()
#     move()
# if right_is_clear():
#     turn_right()
#     keep_moving()


# Around 4:
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def keep_moving():
#     while front_is_clear():
#         move()
#         if object_here():
#             done()
#         if wall_in_front():
#             turn_left()
#             move()
#
#         while right_is_clear():
#             turn_right()
#             move()
#             if wall_in_front():
#                 turn_left()
#                 move()
#
# put()
# if wall_in_front():
#     turn_left()
#     if front_is_clear():
#         move()
#     else:
#         turn_left()
#         move()
#
# if right_is_clear():
#     turn_right()
#     keep_moving()

