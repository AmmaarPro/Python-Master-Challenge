import random
randomlist = []
for i in range(3):
    n = random.randint(1,100)
    randomlist.append(n)

print(randomlist)
randomlist.sort()
print("The Highest Element Is: ", randomlist[-1])