from time import sleep

a = input('Enter first number between 1-1000: ')
b= input('Enter second number between 1-1000: ')

number = 0
sum = 0

for i in range(1000):
  number = number + i
  if number < int(b):
    if number > int(a):
      print(number)
      sum = sum + number

print('_____')
print(sum)
