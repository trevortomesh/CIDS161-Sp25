# # # # # # Print out "Hello, World!" and "My name is Trevor!"
# # # # # # This is a comment! A comment is ignored by the computer!
# # # # # print("Hello, World!")
# # # # # # 10.5+2*3 / 45-3.5
# # # # # print((10.5+2*3) / (45-3.5))
# # # # # # print("My name is Trevor!")
# # # # # # I want this to be a comment!
# # # # # '''
# # # # # This will also be ignored!
# # # # # This can go on for multiple lines... the # can't!
# # # # # '''
# # # #
# # # # # Convert Fahrenheit to Celsius
# # # # # x = 3
# # # # # y = 2
# # # # # z = x + y
# # # # # print(z)
# # # # # print("7 + 5 = ")
# # # # # print(eval("7 + 5"))
# # # # # number = eval(input("Enter a mathematical operation (e.g. 2 + 2 )"))
# # # # # print("Your answer: ", number)
# # # # # newNumber = number + 12
# # # # # print("Your number plus 12 is ", newNumber)
# # # #
# # # # # f = eval(input("Enter degrees Fahrenheit: "))
# # # # # print(str(f) + " degrees Fahrenheit is ")
# # # # # print(str((5 / 9) * (f - 32)) + " degrees Celsius!")
# # # #
# # # # # # Step 1: Prompt the user to enter a radius
# # # # # radius = eval(input("Enter a value for radius: "))
# # # # #
# # # # # # Step 2: Compute Area
# # # # # area = radius * radius * 3.14159
# # # # #
# # # # # # Step 3: Display results
# # # # # print("The area for the circle of radius", radius, "is", area)
# # # # #print("The area for the circle of radius" + str(radius) + "is" + str(area))
# # # #
# # # # # Prompt user to enter three numbers
# # # # number1 = eval(input("Enter the first number: "))
# # # # number2 = eval(input("Enter the second number: "))
# # # # number3 = eval(input("Enter the third number: "))
# # # #
# # # # # Compute Average
# # # # average = (number1 + number2 + number3) / 3
# # # #
# # # # # Print Average
# # # # print("The average of", number1, number2, number3, "is", average)
# # # #
# # # # # don't do this:
# # # # # numberOfCookies = 5
# # # # #3dawg = 3
# # # #
# # # # # a = 5
# # # # # b = 7
# # # #
# # # # # on spacing:
# # # # # do this:
# # # # # x = (1, 2, 3)
# # # # # result = a + b
# # # #
# # # # # don't do this:
# # # # '''
# # # # x = ( 1, 2, 3 )
# # # # result = a+b
# # # # '''
# # # #
# # # # x = 10 # x stores the integer value 10
# # # # y = 3.14 # y stores the floating-point value (decimal) 3.14
# # # # # name = "alice" # name stores the string "alice"
# # # #
# # # # # names of vars must begin with a letter
# # # #
# # # # name = "bob"
# # # # # 1st_name = "bob"
# # # # name_1st = "bob"
# # # #
# # # # # names can contain letters, numbers and underscores
# # # # # nope:
# # # # # name-1st = "bob"
# # # #
# # # # # names cannot be python keywords (like def, class, print, etc.)
# # # # # don't: print = "printyguy"
# # # # # do: print_value = "printguy"
# # # # # don't: class = "classthingy"
# # # # # class_name = "classthingy"
# # # # # don't: def = 4
# # # # # define_function = 4
# # # #
# # # # # names are case-sensitive!
# # # # age = 12
# # # # Age = 12
# # # #
# # # # a = 3
# # # # A = 12
# # # #
# # # # print(a)
# # # # print(A)
# # #
# # # # use descriptive names
# # # # x = 18
# # # num_students = 18 #snake case
# # #
# # # # write snake_case not camelCase
# # # # bad: numStudents = 18 # camel case
# # # # good: num_students = 18
# # #
# # # # avoid single-letter names (unless in specific contexts)
# # # # bad: n = 100
# # # # good: total_count = 100
# # #
# # # # use meaningful names
# # #
# # # # bad: a = "hello world"
# # # # bad: thingy = "hello world"
# # # # bad: my_lumps = "hello world"
# # #
# # # # good: greeting = "hello world"
# # #
# # # # use lower-case with underscores for variables
# # # # good: user_name = "Trevor"
# # # # bad: UserName = "Trevor"
# # # # bad: userName = "Trevor"
# # #
# # # # use upper-case for constants
# # # # Good: PI = 3.14159
# # # # bad: pi = 3.14159
# # #
# # # # avoid using names that clash with built-in functions
# # # #print(sum([1,2,3]))
# # # # bad: sum = sum([1,2,3])
# # # # good: total = sum([1,2,3])
# # # # print(total)
# # #
# # # #no spaces in names
# # # # bad: my variable = 5
# # # # good: my_variable = 5
# # #
# # # # don't use special characters!
# # # # bad: price$ = 10
# # # # good: price_in_dollars = 10
# # # # good: price_value = 10
# # #
# # # variable_guy = 12 # = is the assignment operator
# # #
# # #
# # # t = -16 #what is this?!?!
# # # temp_now = -16 #this is good!
# # # the_temperature_right_now_in_wisconsin_today = -16 #a bit much!
# # #
# # # PI = 3.14159 # upper case is a constant!
# # #
# # # boxy = "I am a box"
# # # print("boxy is currently ", boxy)
# # # boxy = 5
# # # print("boxy is now", boxy)
# # #
# # #
# # # import keyword
# # # print(keyword.kwlist)
# # #
# # # area = 5
# # # Area = 4
# # # aRea = 3
# # # AREA = 2
# # # print(area)
# # # print(AREA)
# #
#
# # PI = 3.14159
# # radius = 1
# # area = radius * radius * PI
# # print(area)
# # radius = 10.0
# # area = radius * radius * PI
# # print(area)
#
#
# # = sign is the "assignment operator"
# # variable = expression
#
# y = 1 # assign 1 to variable "y"
#
# radius = 1.0 # assign 1.0 to variable "radius"
# x = 5 * (3/2) + 3 * 2 # assign the value of the expression to x
# x = y + 1 # assign the addition of y and 1 to x
# area = radius * radius * 3.14159 # compute area
#
# x = 1
# x = x + 1
# #print(x)
#
# i = j = k = 1
# print(i)
# print(j)
# print(k)
# '''
# k = 1
# j = k
# i = j
# '''
from operator import truediv

#####################################################################
# scope: the scope of a variable is the part of the program
#        where the variable can be accessed (or referenced)

# rule: a variable must be created before it can be used!
# radius = 3
# area = radius * radius * 3.14159
# print(area)

###########################################################
# Simultaneous assignment
# var1, var2, ..., varn = exp1, exp2, ..., expn
# x = 1
# y = 2
#
# x, y = y, x
#
# # temp = x
# # x = y
# # y = temp
#
# print("x is now", x)
# print("y is now", y)
#
# print(2//4)
# print(4**0.5)
#
# print(5%2)

# #############################################################
# # Time Converter
#
# # 1. Prompt the user for input
# seconds = eval(input("Enter an integer number of seconds: "))
#
# # 2. Convert to minutes + seconds
# minutes = seconds // 60
# remaining_seconds = seconds % 60
#
# # 3. Output the solution
# print(seconds, "seconds is", minutes, "minutes and",
#       remaining_seconds, "seconds")
#########################################################
# PEMDAS - parenthesis, exponents, multiply, divide, add, subtract
# Evaluating expressions and operator precedence
# x = 5
# y = 3
# a = 1
# b = 2
# c = 3
#
# print((3 + 4 * x) / 5 - 10 * (y - 5) * (a + b + c) / x + 9 * (4 / x + (9+x) / y))
# print(((3 + 4 * x) / 5) - (10 * (y - 5) * (a + b + c)) / x + (9 * (4 / x + (9+x) / y)))

#######################################################################
# Augmented Assignment Operators
#
# a = 0
# print("a was",a)
# # a = a + 1
# a += 2
# print("a is now",a)
#
# # a = a -3
# a -= 3
# print("a is now",a)
#
# # a = a *2
# a *= 2
# print("a is now",a)
#
# # a = a / 2
# a /= 2
# print("a is now",a)
#
#
# a = 3
# # a = a // 2
# a //= 2
# print("a is now",a)
#
# a = 3
# #a = a%2
# a %= 2
# print("a is now",a)
#
# a = 3
# # a = a**2
# a **= 2
# print("a is now",a)

######################################################################
# type conversion / casting
# a = 1
# a = a + 0.5   # cast an into to a float implicitly
# print("a as a float is now",a)
# print("a as an integer is", int(a)) # cast a float to an int explicitly
# # print(3.0//2) # WTF?!?!?!
#
# value = 5.6
# print(round(5.6))

########### DATA TYPES REVIEW #################
# x = 10
# y = -5
# z = 0
#
# print(type(x))
# print(type(y))
# print(type(z))
#
# # Strings
#
# greeting = "Hello, World!"
# name = 'Python'
# multiline = """This is
# a multiline
# string."""
#
# print(type(greeting))
#
# joined = greeting + ' ' + name + ' ' + multiline
# print(joined)

# floats

# a = 3.14
# b = -0.5
# c = 10.0
# d = 0.0
#
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
#
# print(a + b)
# print(0.1 + 0.2)

# # booleans
# a = True
# b = False
# print(type(a))

# complex numbers a + bi
# c1 = 2 + 3j
# c2 = 1 - 4j
#
# print(type(c1))
# print(c1 + c2)

# print(int(3.9))
# print(float(10))
# print(str(42))
# a = 42.0 + 12j
# print("The meaning of life, the universe and everything is " + str(a))
# print(bool(0))
# print(bool(1))
# print(bool("I like eggs!"))
# print(bool(0.0))
# print(bool(100.0))

answer = input("Is it nice out? (True or False)")
if answer == "True":
    print("You should go for a walk!")
