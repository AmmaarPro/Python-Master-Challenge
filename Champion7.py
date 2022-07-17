import random

randomlist = []
oglist = []


for i in range(10):
    n = random.randint(-100,100)
    randomlist.append(n)
    if n > 0:
        oglist.append(n)

print(randomlist)
print(oglist[::-1])