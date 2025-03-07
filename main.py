# calculate the area of a circle:

# radius = eval(input("Input a positive value for radius: "))
# if radius < 0:
#     print("Incorrect input!")
#
# else:
#     area = radius * radius * 3.14159
#     print("Area is", area)

# print(int(True))
# print(int(False))
# print(bool(0))
# print(bool(1))
# print(bool(-1))
#
# val = 0
# if val == 0:
#     print("False")
# else:
#     print("True")
#
# age = 17
# if age >= 18:
#     print("You are allowed to vote!")
# else:
#     print("You are not allowed to vote!")
#
# temperature = 80
# if temperature >= 80:
#     print("It's a hot day!")
# else:
#     print("It's not too hot today!")

# condition1 = False
# condition2 = False
#
# if condition1:
#     # code to execute if condition1 is true
#     print("condition1 is true!")
# elif condition2:
#     #code to execute if condition2 is true
#     print("condition2 is true!")
# else:
#     # code to execute if none of the conditions are true
#     print("No conditions are true!")

# score = eval(input("Enter a score: "))
#
# if score >= 90:
#     print("Grade: A")
# elif score >= 80:
#     print("Grade: B")
# elif score >= 70:
#     print("Grade: C")
# elif score >= 60:
#     print("Grade: D")
# else:
#     print("Grade: F")

# gate1_open = True
# gate2_open = True
# gate3_open = True
#
# if gate1_open:
#     print("Gate 1 has been breeched!")
#     if gate2_open:
#         print("Gate 2 has been breeched!")
#         if gate3_open:
#             print("Gate 3 has been breeched!")
#             print("The King Is Dead!")
#
# temperature = 10
# if temperature > 80:
#     print("It's too hot!")
# else:
#     print("It's not too hot!")

########### ADDITION QUIZ! #################

# import random
#
# # 1) Generate 2 random integers between 0 and 9
# number1 = random.randint(0,9)
# number2 = random.randint(0,9)
#
# # 2) Prompt the user to enter an answer
# answer = eval(input("What is " + str(number1) + " + " + str(number2) + "? "))
#
# # 3) Determine if correct
#
# correct_answer = number1 + number2
# if correct_answer == answer:
#     print("That is correct!")
# else:
#     print("Incorrect! The correct answer is " + str(correct_answer))

######## NON INTEGER RANDOM NUMBERS ###################
import random
print(random.random())