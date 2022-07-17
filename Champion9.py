import random

randomlist = []

for i in range(30):
    n = random.randint(-100,100)
    randomlist.append(n)

randomlist.sort()
print(randomlist)
