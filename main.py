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

gate1_open = False
gate2_open = False
gate3_open = False

if gate1_open == True:
    print("Gate 1 has been breeched!")
    if gate2_open == True:
        print("Gate 2 has been breeched!")
        if gate3_open == True:
            print("Gate 3 has been breeched!")
            print("The King Is Dead!")

temperature = 10
if temperature > 80:
    print("It's too hot!")
else:
    print("It's not too hot!")