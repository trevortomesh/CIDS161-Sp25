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

# continueLoop = 'Y'
# while continueLoop == 'Y' or continueLoop == 'y':
#     continueLoop = input("Would you like to continue? (Y/N):")

data = eval(input("Enter an integer (the input ends if it is 0): "))

sum = 0
while data != 0:
    sum += data
    data = eval(input("Enter an integer (the input ends if it is 0): "))
print("The sum is", sum)