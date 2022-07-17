x = lambda num : 1 if num <= 1 else num*x(num-1)
number = 1

for i in range(100):
    print('%d != %d' %(number, x(number)))
    number = number+1