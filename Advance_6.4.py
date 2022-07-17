a = input('Enter first number within 1 and 1000: ')
b = input('Enter second number within 1 and 1000: ')

def perfectSquares(a, b):

	for i in range(int(a), int(b) + 1):

		if (i**(.5) == int(i**(.5))):
			print(i, end=" ")

perfectSquares(a, b)
