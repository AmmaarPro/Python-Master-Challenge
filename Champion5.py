import random
a_list = []
for i in range(100):
    a_list.append(random.randint(-100, 100))

print(a_list)

def my_max(my_list):
    return sorted(my_list)[-1]

def my_maxx(my_list):
    return sorted(my_list)[-2]

def my_min(my_list):
    return sorted(my_list)[1]

def my_minn(my_list):
    return sorted(my_list)[2]

print('Maximum Two Values')
print(my_max(a_list))
print(my_maxx(a_list))

print('Minimum Two Values')
print(my_min(a_list))
print(my_minn(a_list))