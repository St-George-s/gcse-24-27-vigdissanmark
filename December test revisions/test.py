import random

for counter in range(10):
    elfScore = random.randint (1, 101)
if elfScore <= 50:
    print("child no", counter, "score is", elfScore ,"and is naughty")
else:
    print("child no", counter, "score is",elfScore,"and is good")
