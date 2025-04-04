def sum(i1, i2):
    result = 0
    for i in range(i1,i2+1):
        result += i
    return result

def sayhi():
    return "Hi!"

def sayhello():
    print("Hello!")

def add_stuff():
    a = 2
    b = 2
    c = a + b

def max(num1, num2):
    if num1 > num2:
        sayhello()
        return num1
    else:
        print(sayhi())
        return num2

def main():
    print("Sum from 1 to 10 is", sum(1,10))
    print("Sum from 20 to 37 is", sum(20,37))
    print("Sum from 35 to 49 is", sum(35,49))
    print(sayhi())
    sayhello()
    add_stuff()

    z = max(2,5)
    print(z)
    print(max(1,4))
main() # call the main function

# sum = 0
#
# for i in range(1,11):
#     sum += i
# print("Sum from 1 to 10 is", sum)
#
# sum = 0
#
# for i in range(20, 38):
#     sum += i
# print("Sum from 20 to 38 is", sum)
#
# sum = 0
#
# for i in range(35, 50):
#     sum += i
# print("Sum from 35 to 50 is", sum)
