import random

randomlist = []

for i in range(50):
    n = random.randint(-100,100)
    randomlist.append(n)

randomlist.sort(reverse=True)
print(randomlist)
