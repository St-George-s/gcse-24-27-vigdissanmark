# Data types

name = "vigdis" #This is a string
myAge = 13 #This is an Integer
height = 165.7 #This is a decimal number (float/real)
hasAGuineapig = True #This is a boolean (true/false)

# Casting (change from one data type to another)
age = input("Enter age: ")
print(age)
ageAsAnInt = int(age) #Concentarte two strings together (join them)
print(age + "10")
print(ageAsAnInt + 10) #add two integers together (maths addition)
print("Your age is " + str(ageAsAnInt))

#Data types - more examples
stillAnInteger = -4
myNumber = "08754327" # always store as a string

# Arithmetic operators
add = 10 + 10
subtract = 10 - 10
multiply = 10 * 10
divide = 10 / 10 #Will output a float
integerDivision = 11 // 10 #forces output to be an integer
print(add, subtract, multiply, divide)
print(integerDivision)
modulo = 5 % 4 #remainder of the division
print(modulo)
exponent = 2 ** 3 # to the power of
print(exponent)

# Activity 1 - take two inputs, multiply them together and output answer
number1 = input("Enter a number: ")
number2 = input("Enter a number: ")

multiply = int(number1) * int(number2)
print(multiply)
# Activity 2 - input users age, output times age time 7

# Activity 3 - take radius as input, output volume of sphere (v = 4/3 x pi x r^3)