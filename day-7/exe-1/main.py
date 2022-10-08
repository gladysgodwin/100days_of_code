import random

lists = ["gladys", "michael", "choja"]

ran = random.choice(lists)
print(ran)

user = input("Enter a letter\n")

for n in ran:
    if n == user:
        print("good")
    else:
        print("wrong")
