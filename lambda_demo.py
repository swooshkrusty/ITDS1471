#lambda examples 

test = lambda x: x + 3

print(f"Lambda with one argument: {test(5)}")

# lambda with two arguments
test_2_arg = lambda x, y: x*y
print(f"Lambda with two arguments: {test_2_arg(5, 3)}")  # Output: 15

# lambda in sorting
ids = ['id1', 'id2', 'id10', 'id20', 'id22', 'id30']
points = [(3, 1), (5, 4), (2, 3)]
sorted_ids = sorted(ids)
print(f"Original IDs: {ids}\nSorted IDs: {sorted_ids}") 
sorted_ids_lambda = sorted(ids, key=lambda id: int(id[2:]))
print(f"Original IDs: {ids}\nSorted part of the id: {sorted_ids_lambda}")  # Output: ['id1', 'id2', 'id10', 'id20', 'id22', 'id30']

#another example of lambda in sorting

lst= [[14,22,3],[31,35,6],[27,18,9]]
sorted_lst = sorted(lst, key=lambda x: x[1])
print(f"Original list: {lst}\nSorted list:{sorted_lst}")

sorted_lst_lambda = lambda x:[sorted(sublist) for sublist in x]

print(f"Original list: {lst}\nSorted sublist:{sorted_lst_lambda(lst)}")

#test yourself - sort a list of tuples

scores = [('Python', 90), ('Java', 80), ('C++', 93)]

sorted_scores = sorted(scores)

print(f"Original scores: {scores}\nSorted scores: {sorted_scores}")  # Output: [('C++', 93), ('Java', 90), ('Python', 90)]

sorted_scores_lambda = sorted(scores, key=lambda t: t[1], reverse=True)
print(f"Original scores: {scores}\nSorted scores using lambda: {sorted_scores_lambda}")  # Output: [('C++', 93), ('Python', 90), ('Java', 80)]

# more examples of lambda functions

fruit_list = ['apple', 'orange', 'kiwi', 'mango']

new_fruit_list = lambda y:[x.capitalize() for x in y]

print(f"list with all capitalized letters: {new_fruit_list(fruit_list)}")  # Output: ['Apple', 'Orange', 'Kiwi', 'Mango']

any_function = lambda y, func: [func(x) for x in y]

print(f"Uppercase string: {any_function(fruit_list, str.upper)}")  # Output: ['Apple', 'Orange', 'Kiwi', 'Mango']
print(f"Lowercase string: {any_function(fruit_list, str.lower)}")  # Output: ['apple', 'orange', 'kiwi', 'mango']
print(f"Capitalized string: {any_function(fruit_list, str.capitalize)}")  # Output: ['Apple', 'Orange', 'Kiwi', 'Mango']
print(f"Size of list: {any_function(fruit_list, len)}")  # Output: [5, 6, 4, 5]

# map, filter with lambda

def double_value(num):
    return num * 2
nums = [num for num in range(1, 11)]

doubled_nums = map(double_value, nums)

print(f"Using map:{doubled_nums}")  # Output: <map object at 0x7f8b8c8c8c8c>

print(f"Using map with list: {list(doubled_nums)}")  # Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

doubled_nums_lambda = list(map(lambda x: x * 2, nums))

print(f"Using map with lambda: {doubled_nums_lambda}")  # Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

#another example using list of tuples

names = [('John', 'Smith'), ('Mary', 'Johnson'), ('Tim', 'Cook')]

full_names = list(map(lambda t: f"{t[0]} {t[1]}", names))
print(f"Full names: {full_names}")  # Output: ['John Smith', 'Mary Johnson', 'Tim Cook']

#filter examples

def is_even(num):
    return num % 2 == 0
even_list = list(filter(is_even, nums))

print(f"Even list: {even_list}")  # Output: [2, 4, 6, 8, 10]

even_list_lambda = list(filter(lambda x: x % 2 == 0, nums))
print(f"Even list using lambda: {even_list_lambda}")  # Output: [2