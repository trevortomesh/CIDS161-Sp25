import turtle
from GCDFunction import *
#
# #y = 3
# x = 1
# globalVar = 1
# def f1():
#     x = 2
#     print(x)
#
# def f2():
#     localVar = 2
#     print(globalVar)
#     print(localVar)
#
# def increase():
#     global x
#     x = x + 1
#     print(x)


# def sum(a = 0,b = 0):
#     return a+b
#
# def printArea(width = 1, height = 2):
#     area = width * height
#     print("width:",width,"\theight:",height,"\tarea:",area)

def sort(number1, number2):
    if number1 < number2:
        return number1, number2
    else:
        return number2, number1

def main():
    #print(sort(3,3))

    # letter = 'A' #same thing as letter = "A"
    # numberChar = "4"
    # a = 4
    # print(int(numberChar) + a)
    # print(letter)
    # print(numberChar)
    # print("Hello"+"World")
    #
    # print("\u6B22\u8FCE \u03b1 \u03b2 \u03b3")
    # ch = 'a'
    # print(ord(ch))
    #
    # print(chr(0))
    # print(chr(1))
    #
    # for i in range(0,127):
    #     print(str(i) + " is " + chr(i))
    #
    # print(ord('a') - ord('A'))
    # offsest = ord('a') - ord('A')
    # lowercaseLetter = 'h'
    # uppercaseLetter = chr(ord(lowercaseLetter) - offsest)
    # print(uppercaseLetter)
    # print("Is this \nthe real life?")
    # print('Trevor\'s tugboat')
    # print("Trevor said, \"That\'s my tugboat!\"")
    #
    # print("Is this the real life?", end='\t')
    # print("Is this just fantasy?")
    #
    # number = input("Give me a number: ")
    # s = str(eval(number) * 3.14159)
    # #s = str(3.4) # convert a float into a string
    # print(str(number) +" * pi " + " is " + s)
    #
    #
    # s1 = input("Enter a string: ")
    # s2 = input("Enter a string: ")
    # s3 = input("Enter a string: ")
    # print("s1 is " + s1)
    # print("s2 is " + s2)
    # print("s3 is " + s3)

    # print(sum())
    # print(sum(3,3))
    # printArea(3,3)
    # printArea()
    # printArea(height = 5, width = 3)
    # printArea(width=3)
    # printArea(height=4)



    # increase()
    # print(x)

    # sum = 0
    # for i in range(5):
    #     sum += i
    # print(i)

    # x = eval(input("Enter a number: "))
    # if x > 0:
    #     y = 4
    #
    # print(y)

    #f2()
    #print(globalVar)
    #print(localVar)
    #print("test")
    #f1()
    #print(x)


    amount = 12618.98
    interestRate = 0.0013
    interest = amount * interestRate
    print("Interest is", format(interest, "10.2f"))
    print(format(57.467657,".2f"))
    print(format(57.467657, "10.2f"))
    print(format(57.467657, "10.2e"))
    print(format(0.0033923,"10.2e"))

    print(format(0.53457,"10.2%"))
    print(format(57,"10.2%"))
    print(format(57.467657, "10.2f"))
    print(format(57.467657, "<10.2f") + "things")

    a = 59832
    b = 12312
    print(format(a, "10d"))
    print(format(a, "<10d"))
    print(format(a, "<10o") + format(b,"x"))

    print(format("I like eggs!", ">20s"))
    print(format("I like green eggs and ham!",">20s"))

if __name__ == "__main__":
    main()
