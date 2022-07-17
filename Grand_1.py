import random
import collections

randomlist = []

for i in range(1000):
    n = random.randint(1,5)
    randomlist.append(n)

print(randomlist)
print([item for item, count in collections.Counter(randomlist).items() if count > 1])
print(sum([item for item, count in collections.Counter(randomlist).items() if count > 1]))
