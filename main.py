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
    print(sort(3,3))

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


if __name__ == "__main__":
    main()
