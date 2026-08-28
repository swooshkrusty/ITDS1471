lst = [0] * 10

print(lst)

lst.append(5)
print(lst)
print(f"List elements: {lst}")

lst[0] = 24
print(lst)
print(f"List elements after update: {lst}")

#use random numbers 1-100
import random

for i in range(len(lst)):
    lst[i] = random.randint(1, 100)
print(f"List elements with new random numbers: {lst}")

#append data

for i in range(10):
    lst.append(random.randint(1, 100))
print(f"List elements after appending new random numbers: {lst}")


#append, extend data

lst1 = [1,2,3]
lst.append(lst1)
print(f"List elements after appending lst1: {lst}")

lst.extend(lst1)
print(f"List elements after extending with lst1: {lst}")


#list comprehension
new_list = [random.randint(1, 100) for _ in range(5)]
print(f"New list elements: {new_list}")

# print list 

for i in range(len(new_list)):
    print(f"{new_list[i]}", end=" ")
print()

for num in new_list:
    print(f"{num}", end=" ")
print()

print()

sorted_list = sorted(new_list)
print(f"Sorted list:{sorted_list}")
print(f"The max value of one-dim list:{max(new_list)}")
print(f"The sum of one-dim list:{sum(new_list)}")
print(f"The min value of one-dim list:{min(new_list)}")

# two-dim list
two_dim = [[random.randint(1, 100) for _ in range(5)] for _ in range(3)]
print(f"two-dim list:{two_dim}")

# locate the max value of each row

max_rows = [max(row) for row in two_dim]
print(f"Max value of each row: {max_rows}")

# locate the max value of the entire two-dim list
max_value = max(max(row) for row in two_dim)
print(f"Max value of the entire two-dim list: {max_value}")
min_value = min(min(row) for row in two_dim)
print(f"Min value of the entire two-dim list: {min_value}") 

# locate the max value of each row
max_rows = [max(row) for row in two_dim]
print(f"Max value in each row:{max_rows}")
max_value = max(max_rows)

# get min value of each row
min_rows = [min(row) for row in two_dim]
print(f"Min value in each row:{min_rows}")
min_value = min(min_rows)

# locate the max value for each column
max_cols = [max(col) for col in zip(*two_dim)]



"""Dictionary"""

d = {}
d = {'one': 1, 'two': 2, 'three': 3}
print(f"Dictionary elements: {d}")
print(f"Value for key 'one': {d['one']}")

d['three'] = 5
print(f"Dictionary elements after update: {d}")

for key, value in d.items():
    print(f"Key: {key}, Value: {value}")

d2 = {}

for key, value in d.items():
    d2[value] = key
print(f"Dictionary d2 elements: {d2}")