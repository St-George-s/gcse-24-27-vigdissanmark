# # example
# for counter in range(10):
#     print("hi")
#     # question 1
# yourname = input("Enter your name: ")
# for counter in range(1000):
#     print(yourname)
#     #question 2
# yourname = input("Enter your name: ")
# for counter in range(1000):
#     print("Hello", yourname)
#question 4 and 5 
# for counter in range (1, 1001):
#     print(counter * 8)
#question 6
# for counter in range (1,13):
#     print("7 x", counter, "=", counter * 7)
# question 7
# for counter in range(10):
#     age = input("Enter an age: ")
#     print(age)
#question 8
# for counter in range(10):
#     age = int(input("Enter and age: "))
#     print(age * 10)
#question 9 
# total = 0
# for counter in range(10):
#      age = int(input("Enter an age: "))
#      total = total + age
#      print(total)
#question 10
# for counter1 in range(1,13):
#     for counter2 in range(1,13): 
#         print (counter1, " X ", counter2,"=", counter1 * counter2)

#extension
timesTable = int(input("Which TT?: "))
howFar = int(input("How Far?:  "))

for counter in range(1, howFar+1):
    print(counter * timesTable)