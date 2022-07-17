from random import randint
value=0
x=0

for _ in range(10):
	value = randint(0, 100)
	x = value+x
	print(value)

print('______')
print(x)
print('x2')
print('______')
print(x*2)
