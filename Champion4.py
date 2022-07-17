import random

randomlist = []
oglist = 0


for i in range(100):
    n = random.randint(-100,100)
    randomlist.append(n)
    if n > 0:
        oglist = oglist+n

print(randomlist)
print(oglist)