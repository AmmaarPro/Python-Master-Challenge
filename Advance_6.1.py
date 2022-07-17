a = input('Enter first number between 1-1000: ')
b = input('Enter second number between 1-1000: ')

lower = a
upper = b
for i in range(int(lower), int(upper)+1):
   if(i%2==1):
      print(i)