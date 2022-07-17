import random
randomlist = []
for i in range(100):
    n = random.randint(-100,100)
    randomlist.append(n)

print(randomlist)
randomlist.sort()
print("The Highest Is: ", randomlist[-1])
print("The Lowest Is: ", randomlist[-100])
print("Differance Between Highest & Lowest Is:", randomlist[-1]-randomlist[-100])
