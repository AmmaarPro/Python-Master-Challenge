from random import randint

n1 = randint(0, 10000)
n2 = randint(0, 10000)
print(n1, n2)
if n1<n2:
    print(n1, 'is smaller than', n2)
elif n1>n2:
    print(n2,'is smaller than', n1)
elif n1==n2:
    print('Both', n1 ,'and',n2,'are equal')