from random import randint

num_bushes = int(input('Enter the number of bushes: '))
list_1 = [randint(5, 10) for _ in range(num_bushes)]
print(list_1)

a = int(input('Enter the bush number: '))
res = 0

if a == 1:
    res = list_1[0] + list_1[1] + list_1[-1]
elif a == num_bushes:
    res = list_1[-2] + list_1[-1] + list_1[0]
else:
    res = list_1[a - 1] + list_1[a - 2] + list_1[a]

print(res, 'berries')