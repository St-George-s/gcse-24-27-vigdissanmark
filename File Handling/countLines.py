with open("/workspaces/gcse-24-27-vigdissanmark/File Handling/holiday.txt", "r") as file:
    counter = 0
    for line in file:
        print(line)
        counter = counter + 1
        print("There are ",counter, "lines")