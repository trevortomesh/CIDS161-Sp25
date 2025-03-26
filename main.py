# import random
#
# # 1) Generate a random number to be guessed
# number = random.randint(0,100)
# guess = -1
#
# while guess != number:
#     # 2) Prompt the user for input
#     print("Guess a number between 0 and 100!")
#     guess = eval(input("Enter your guess: "))
#
#     # 3) Determine if the number is higher, lower or et the guess
#
#     if guess == number:
#         print("Yes! The number is", number)
#     elif guess > number:
#         print("Your guess is too high!")
#     else:
#         print("Your guess is too low!")
import time

# continueLoop = 'Y'
# while continueLoop == 'Y' or continueLoop == 'y':
#     continueLoop = input("Would you like to continue? (Y/N):")

# data = eval(input("Enter an integer (the input ends if it is 0): "))
#
# sum = 0
# while data != 0:
#     sum += data
#     print("this is in the while loop!")
#     data = eval(input("Enter an integer (the input ends if it is 0): "))
#
# print("this is not!")
# print("The sum is", sum)

# count = 0
# while count <= 100:
#     print(count)
#     count = count + 1
#

# for variable in sequence
# for i in range(100, 0, -1):
#     print(i)

# for beers in range(99, 0, -1):
#     if beers == 1:
#         print(beers, "bottle of beer on the wall")
#         print(beers, "bottle of beer!")
#         print("Take one down, pass it around...")
#         print(beers - 1, "bottles of beer on the wall!")
#         print("*******************************")
#
#     else:
#         print(beers, "bottles of beer on the wall")
#         print(beers, "bottles of beer!")
#         print("Take one down, pass it around...")
#         print(beers-1 , "bottles of beer on the wall!")
#         print("*******************************")

# count = 0
# while count < 5:
#     count2 = 0
#     while count2 < 3:
#         print(count2)
#         count2 = count2 + 1
#     count = count + 1
#     print("count is: ", count)

# print("Hello World!")

# for hours in range(0,24):
#
#     for minutes in range(0,60):
#         for seconds in range(0,60):
#             print("It has been ",hours, " hours ", minutes, " minutes and ",
#                   seconds, " seconds")
#             time.sleep(1)

# sum = 0
# number = 0
#
# while True:
#     number += 1
#     sum += number
#
#     if sum >= 100:
#         break
#
#     print("The number is ", number)
#     print("The sum is", sum)

# print("This program prints Let's-a-go! until you say stop!")
# while True:
#     print("Let's-a-go!")
#     go_again = input("Should Mario go again? (y/n)")
#     if go_again != "y":
#         break

sum = 0
number = 0

while number < 20:
    number += 1
    if number == 10 or number == 11:
        continue
    sum += number
    print("The number is now", number)
    print("The sum is now ", sum)
