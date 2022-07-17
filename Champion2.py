n = int(input('Enter number to find divisors: '))

i = 1
while i <= n:
    if (n % i == 0):
        print (i)
    i = i + 1

