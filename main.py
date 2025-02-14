# # # Print out "Hello, World!" and "My name is Trevor!"
# # # This is a comment! A comment is ignored by the computer!
# # print("Hello, World!")
# # # 10.5+2*3 / 45-3.5
# # print((10.5+2*3) / (45-3.5))
# # # print("My name is Trevor!")
# # # I want this to be a comment!
# # '''
# # This will also be ignored!
# # This can go on for multiple lines... the # can't!
# # '''
#
# # Convert Fahrenheit to Celsius
# # x = 3
# # y = 2
# # z = x + y
# # print(z)
# # print("7 + 5 = ")
# # print(eval("7 + 5"))
# # number = eval(input("Enter a mathematical operation (e.g. 2 + 2 )"))
# # print("Your answer: ", number)
# # newNumber = number + 12
# # print("Your number plus 12 is ", newNumber)
#
# # f = eval(input("Enter degrees Fahrenheit: "))
# # print(str(f) + " degrees Fahrenheit is ")
# # print(str((5 / 9) * (f - 32)) + " degrees Celsius!")
#
# # # Step 1: Prompt the user to enter a radius
# # radius = eval(input("Enter a value for radius: "))
# #
# # # Step 2: Compute Area
# # area = radius * radius * 3.14159
# #
# # # Step 3: Display results
# # print("The area for the circle of radius", radius, "is", area)
# #print("The area for the circle of radius" + str(radius) + "is" + str(area))
#
# # Prompt user to enter three numbers
# number1 = eval(input("Enter the first number: "))
# number2 = eval(input("Enter the second number: "))
# number3 = eval(input("Enter the third number: "))
#
# # Compute Average
# average = (number1 + number2 + number3) / 3
#
# # Print Average
# print("The average of", number1, number2, number3, "is", average)
#
# # don't do this:
# # numberOfCookies = 5
# #3dawg = 3
#
# # a = 5
# # b = 7
#
# # on spacing:
# # do this:
# # x = (1, 2, 3)
# # result = a + b
#
# # don't do this:
# '''
# x = ( 1, 2, 3 )
# result = a+b
# '''
#
# x = 10 # x stores the integer value 10
# y = 3.14 # y stores the floating-point value (decimal) 3.14
# # name = "alice" # name stores the string "alice"
#
# # names of vars must begin with a letter
#
# name = "bob"
# # 1st_name = "bob"
# name_1st = "bob"
#
# # names can contain letters, numbers and underscores
# # nope:
# # name-1st = "bob"
#
# # names cannot be python keywords (like def, class, print, etc.)
# # don't: print = "printyguy"
# # do: print_value = "printguy"
# # don't: class = "classthingy"
# # class_name = "classthingy"
# # don't: def = 4
# # define_function = 4
#
# # names are case-sensitive!
# age = 12
# Age = 12
#
# a = 3
# A = 12
#
# print(a)
# print(A)

# use descriptive names
# x = 18
num_students = 18 #snake case

# write snake_case not camelCase
# bad: numStudents = 18 # camel case
# good: num_students = 18

# avoid single-letter names (unless in specific contexts)
# bad: n = 100
# good: total_count = 100

# use meaningful names

# bad: a = "hello world"
# bad: thingy = "hello world"
# bad: my_lumps = "hello world"

# good: greeting = "hello world"

# use lower-case with underscores for variables
# good: user_name = "Trevor"
# bad: UserName = "Trevor"
# bad: userName = "Trevor"

# use upper-case for constants
# Good: PI = 3.14159
# bad: pi = 3.14159

# avoid using names that clash with built-in functions
#print(sum([1,2,3]))
# bad: sum = sum([1,2,3])
# good: total = sum([1,2,3])
# print(total)

#no spaces in names
# bad: my variable = 5
# good: my_variable = 5

# don't use special characters!
# bad: price$ = 10
# good: price_in_dollars = 10
# good: price_value = 10

variable_guy = 12 # = is the assignment operator

the_temperature_right_now_in_wisconsin_today = 23












