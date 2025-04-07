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

# print grade for a given score
def printGrade(score):
    if score >= 90.0:
        print('A')
    elif score >= 80.0:
        print('B')
    elif score >= 70.0:
        print('C')
    elif score >= 60.0:
        print('D')
    else:
        print('F')

# print grade for a given score
def getGrade(score):
    if score >= 90.0:
        return 'A'
    elif score >= 80.0:
        return 'B'
    elif score >= 70.0:
        return 'C'
    elif score >= 60.0:
        return 'D'
    else:
        return 'F'
