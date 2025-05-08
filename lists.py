# ages = [36, 22, 23, 21, 19, 21, 51, 32]
#
# average = sum(ages) / len(ages)
#
# print("The average age in our class is: ", average)
# print("The max age is: ", max(ages))
# print("The min age is : ", min(ages))
#
# print("Dr. T's age is: ", ages[0])
# print("The length of the list is: ", len(ages))
# print("The last element in the list is: ", ages[len(ages)-1])
#
# print("The age range is: ", max(ages)-min(ages))
# maxAge = max(ages)
# minAge = min(ages)
#
# firstAge = ages[0]
# lastAge = ages[7]
# print(firstAge - lastAge)
#
# ages[0] = 42
#
# print(ages)
#
# for i in range(len(ages)):
#     ages[i] = i
# print(ages)
#
# print(ages[len(ages)-2])
# print(ages[-2])

#list1 = [2,3,5,2,33,21]
#print(len(list1))
#print(list1[len(list1)-3])
#print(list1[-3])


#print(list1[2:5])
#print(list1[1:5])
#print(list1[0:3])
#print(list1[:3])
#print(list1[3:len(list1)])
#print(list1[3:])


# list1 = [2,3]
# list2 = [1,9]
#
# list3 = list1+list2
# print(list3)
# # string1 = "Hello"
# # string2 = "World"
# # string3 = string1+string2
# # print(string3)
#
# list4 = 3 * list1
# print(list4)
#
# print(33 not in list4)
# print(2 in list4)
#
# print(list4)
#
# # for u in list4:
# #     print(u)
#
# for i in range(0, len(list4), 2):
#     print(list4[i])

# list1 = ["green", "red", "blue"]
# list2 = ["red", "blue", "green"]
# list4 = ["red", "blue", "green"]
# list3 = [1,2,3]
#
# print(list1 == list2)
# print(list3 != list1)
# print(list2 == list4)
# print(list1 < list2)
#
# abclist1 = ["b","a","c"]
# abclist2 = ["a", "b", "c"]
#
# print(abclist1 < abclist2)

#list1 = [0,1,2,3,4]
list1 = [2*x for x in range(5)]
print(list1)
list2 = [0.5*x for x in list1]
print(list2)