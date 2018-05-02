
# python
# learning the basics of the Python from Lynda (lynda.com)
# also learning git

# chapter 8 lesson 1
# Basic Data Structures

# the list type - it is mutable
x_list = [1,2,3,4,5]

# the tuple type - it is inmutable
x_tuple = (1,2,3,4,5)

# the dictionary type - a key of values and pairs
X_dict_1 = dict(a=1, b=2, c=3, d=4, e=5)
x_dict_2 = {'a': 1, 'b': 2, 'c': 3, 'd':4, 'e':5}

# the set type - an unordered list of unique values
x_set = {1, 2, 5, 7, 10, 8, 10}

print(type(x_list))
print(type(x_tuple))
print(type(X_dict_1))
print(type(x_dict_2))
print(type(x_set))

for myItem in x_set:
    print(myItem)
