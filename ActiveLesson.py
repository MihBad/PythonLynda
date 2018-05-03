
# python and github
# learning the basics of the Python from Lynda (lynda.com)
# also learning git

# --------------------------------------
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


# --------------------------------------
# chapter 8 lesson 2
# Lists and Tuples

def main_8_2():
    game = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
    game_2 = ('Rock', 'Paper', 'Scissors', 'Lizard', 'Spock')   
    i = game.index('Paper')
    print(i)
    game.append('Computer')
    game.insert(0, 'laptop')
    # game.remove('Lizard') # removes the Lizard from the list
    del game[3] # removes Scissors (not Lizard) because laptop was inserted as element 0
    del game[1:3] # remove by slice (elements 1 and 2, so 1:3 non inclusive)
    print_list(game)
    x_pop = game.pop()
    print('Item removed from list: {}'.format(x_pop))
    x_list_joined = ', '.join(game_2)
    print('List with join character: {}'.format(x_list_joined))
    print_list(game)
    print(len(game))
    print(len(game_2))

def print_list(o):
    for i in o:
        print(i, end=' ', flush=True)
    print()

# if __name__=='__main__': main_8_2()

# --------------------------------------
# chapter 8 lesson 3
# Dictionaries

def main_8_3():
    # the code for lesson 3 in chapter 8
    animals = dict(kitten='meow', puppy='ruff', lion='grrrr', giraffe='I am a girrafe!', dragon='rawr')
    # animals = {'kitten': 'meow', 'puppy': 'ruff', 'lion': 'grrrr'
    #             , 'giraffe': 'I am a girrafe!', 'dragon': 'rawr'}
    
    animals['lion']='I am a lion!' # change the lion value
    animals['monkey']='haha'
    # print(animals['godzilla']) # exception is raised = KeyError when the key does not exists in the dictionary
    print(animals.get('godzilla')) # no exception is raised if the key doesn't exist
    print(animals.get('lion')) # no exception is raised if the key doesn't exist
    # for k in animals.keys(): print(k)
    # print()
    # for v in animals.values(): print(v)
    # print()
    # print_dict(animals)

def print_dict(o):
    for x in o:
        print(f'{x}: {o[x]}') # the dictionary in outputted as a list element with syntax: o[x]

# if __name__=='__main__': main_8_3()

# --------------------------------------
# chapter 8 lesson 4
# Sets

def main_8_4():
    # the code for lesson 4 in chapter 8
    a = set('abcde')
    b = set('defgh')
    # print_set(sorted(a))
    # print_set(sorted(b))
    print_set(sorted(a-b)) # members from set a but not in set b
    print_set(sorted(b-a)) # members in b but not in a
    print_set(sorted(a|b)) # members in a or b
    print_set(sorted(a^b)) # members that are in a or b
    print_set(sorted(a&b)) # members that are in both a and b

def print_set(pSet):
    # print a set easily
    print('{', end='')
    for oneSet in pSet:
        print(f'{oneSet}', end='', flush=True)
    print('}')

# if __name__=='__main__': main_8_4()

# --------------------------------------
# chapter 8 lesson 5
# List Comprehension

def main_8_5():
    # function for the lesson 5 in chapter 8
    from math import pi
    seq = range(11)
    seq2 = [x for x in seq if x % 3 != 0] # this will be the double of the elements in x
    seq2_2 = [(x, x**2) for x in seq] # a new list with tuples for each x element and x squared
    seq2_fib = [(x, x) for x in seq] # should be the fibonacci sequence but I can't make it on one line
    seq2_rounding_to_pi = [round(pi, i1) for i1 in seq] # round pi to i number of digits
    seq2_dict={i2:round(pi, i2) for i2 in seq}
    seq_set = {x for x in 'superduper' if x not in 'pd'}
    print_list_85(seq)
    print_list_85(seq2)
    print_list_85(seq2_2)
    print_list_85(seq2_rounding_to_pi)
    print(seq2_dict)
    print(seq_set)
    print_list_85(sorted(seq_set))


def print_list_85(o):
    for x in o:
        print(x, end=' ')
    print()

if __name__=='__main__': main_8_5()