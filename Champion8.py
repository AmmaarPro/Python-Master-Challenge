import random

randomlist = []
oglistev = []
oglistod = []


for i in range(100):
    n = random.randint(-100,100)
    randomlist.append(n)
    if n > 0:
        if n%2==0:
            oglistev.append(n)
        else:
            oglistod.append(n)

print(randomlist)
print('Even')
print(oglistev)
print('Odd')
print(oglistod)