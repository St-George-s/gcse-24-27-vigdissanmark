swimTime = float(input("Enter a swim time: "))
if swimTime < 55.0:
    print("Participant qualifies for Gold category")
elif swimTime > 55.0 and swimTime < 60.0:
    print("Participant qualifies for Silver category")
elif swimTime > 60.0 and swimTime < 65.0:
    print("Participant qualifies for bronce category")
else:
    print("Participant does not qualify")