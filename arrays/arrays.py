#create arrays
heights = [2.4, 3.8, 0.4, 1.9]
names = ["bob", "dave", "simon", "john"]

print(names[1]) #prints dave
print(heights[1])#prints 3.8

#loop names over an array and print
for counter in range(len(names)):
    print(names[counter]) #counter is 0 then  1 then 2
    print(heights[counter])

#append (add) to an array
heights.append(2.2)
names.append("jimmy")

print(heights)
print(names)