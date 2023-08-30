from random import randint

n_set = set(randint(1, 10) for i in range(int(input('Enter the number of elements of the first set: '))))
print(n_set)

m_set = set(randint(1, 10) for i in range(int(input('Enter the number of elements of the second set: '))))
print(m_set)

if not n_set & m_set:
    print("No intersections between the sets.")
else:
    a_set = sorted(n_set & m_set)
    print("Intersection:", *a_set)