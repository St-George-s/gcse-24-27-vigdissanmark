#procedure with one parameter name
# def printName(name):
#     print(name)

# #Function with one parameter name
# def printNameFunc(name):
#     return name

# #call the procedure
# printName("Sanveen")

# #call the function and print a returned value
# print(printNameFunc("Vichy"))

# #call the function and store returned value in a variable
# returnedName = printNameFunc("Emby")
# print(returnedName)

#q4
# def sphere_volume(radius):
#     sphere_volume = (4/3 * 3.14 * (radius)**3)
#     return sphere_volume

# print(sphere_volume(67))

# volume = sphere_volume(5) 
# print(volume)

def linear_search(data_list, target):
    for data_list in data_list:
        if data_list == target:
            return True
    return False

data_list = [3, 8, 2, 10, 7]
print(linear_search(data_list, 10))
