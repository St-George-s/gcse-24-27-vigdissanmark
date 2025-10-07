#quetsion 1 + 3 parrallel arrays
cityNames = ["london", "edinburgh", "cardiff", "belfast", "glasgow"]
population = [8908, 482, 366, 341, 635]
# for counter in range(len(cityNames)):
#     print(cityNames[counter] + "has a population of" + str(population[counter]))

#linear search
found = False
userCity = input("what city would you like the population for?: ")
for counter in range(len(cityNames)):
    if userCity == cityNames[counter]:
        print(cityNames[counter] + "has a population of" + str(population[counter]))
        found = True 

if not found:
    print("your city was not found")
