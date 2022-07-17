list = []

n1=input('Enter Number 1: ')
n2=input('Enter Number 2: ')
n3=input('Enter Number 3: ')
list.append(n1)
list.append(n2)
list.append(n3)

print(list)
list.sort()
print("The Largest Element Is: ", list[-1])