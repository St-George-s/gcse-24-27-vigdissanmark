tooShort = True
hasSpecialChar = True
hasSpace = True

while tooShort or hasSpace or hasSpecialChar:
    # Checks length
    userName = input("enter a username: ")
    tooShort = False
    if len(userName) < 5:
        tooShort = True
        print("too short")

    #Checks for space
    hasSpace = False
    for counter in range(len(userName)):
        if userName[counter] == " ":
            hasSpace = True

    if hasSpace == True:
        print("cant contain spaces")

    #Checks for special char
    hasSpecialChar = False
    for char in userName:
        asciiVal = ord(char)
        if((asciiVal >= 33 and asciiVal <= 47) or 
        (asciiVal >= 58 and asciiVal <= 64) or 
        (asciiVal >= 91 and asciiVal <= 96) or 
        (asciiVal >= 123 and asciiVal <= 127)):
                hasSpecialChar = True
    if hasSpecialChar == True:
        print("contains special character")

print("accepted")