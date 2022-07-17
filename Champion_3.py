def compute_lcm(x, y):

   if x > y:
       great = x
   else:
       great = y

   while(True):
       if((great % x == 0) and (great % y == 0)):
           lcm = great
           break
       great += 1

   return lcm

n1 = input('Enter number 1: ')
n2 = input('Enter number 2: ')

print("The LCM. is", compute_lcm(int(n1), int(n2)))