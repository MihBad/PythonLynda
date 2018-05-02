
# python
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
# chapter 8
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

if __name__=='__main__': main_8_2()