print("If you want to convert Fahrenheit to Celsius [press 1]")
print("If you want to convert Celsius to Fahrenheit [press 2]")
print("If you want to exit [press3]")
i = input('Enter Number: ')
print('\033[1m''Option',i,'has been chosen''\033[0m')
if i == '1':
      fahrenheit = float(input("Enter temperature in fahrenheit: "))
      celsius = (fahrenheit - 32) * 5 / 9
      print('%.2f Fahrenheit is: %0.2f Celsius' % (fahrenheit, celsius))
elif i =='2':
      celsius = float(input("Enter temperature in celsius: "))
      fahrenheit = (celsius * 9/5) + 32
      print('%.2f Celsius is: %0.2f Fahrenheit' %(celsius, fahrenheit))
elif i =='3':
      exit()

