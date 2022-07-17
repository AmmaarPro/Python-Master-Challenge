import random
randomlist = []
for i in range(10):
    n = random.randint(1,100)
    randomlist.append(n)

print(randomlist)
randomlist.sort()
print("The Highest Mark Is: ", randomlist[-1])