import cmath

a = input('Enter a: ')
b = input('Enter b: ')
c = input('Enter c: ')

d = (int(b)**2) - (4*int(a)*int(c))

sol1 = (-int(b)-cmath.sqrt(int(d)))/(2*int(a))
sol2 = (-int(b)+cmath.sqrt(int(d)))/(2*int(a))

print('The solution are {0} and {1}'.format(sol1,sol2))