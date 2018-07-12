
# python and github
# learning the basics of the Python from Lynda (lynda.com)
# official name: Python Essential Training with Bill Weinman
# https://www.linkedin.com/learning/python-essential-training-2
# also learning git
# Martin arrived

import sys

print('\n'*3)
print('--- code starts here ---> ')


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

# if __name__=='__main__': main_8_5()


# --------------------------------------
# chapter 8 lesson 6
# Mixed Structures
# incomplete due to repetitive tasks - easy to understand

# globals
dlevel=0 # manage nesting level

def main_8_6():
    # code for lesson 6 in chapter 8
    r=range(11)
    l=[1, 'two', 3, {'4': 'four'}, 5]
    t=('one', 'two', None, 'four', 'five')
    s=set("It's a bird! It's a plane! It's Superman!")
    d=dict(one=r, two=l, three=s)
    mixed=[l, r, s, d, t]
    disp(mixed)

def disp(o):
    global dlevel

    dlevel += 1
    if isinstance(o, list):
        print_list_86(o)
    elif isinstance(o, range):
        print_range_86(o)
    # elif isinstance(o, tuple):
    #     print_tuple_86(o)
    # elif isinstance(o, set):
    #     print_set_86(o)
    # elif isinstance(o, dict):
    #     print_dict_86(o)
    elif o is None:
        print('Nada', end=' ', flush=True) 
    else:
        print(repr(o), end=' ', flush=True)
    dlevel -= 1

    if dlevel <=1:
        print() # new line after outer

def print_list_86(parList):
    if len(parList)==0:
        print('The list is empty.')
    else:
        print('The list items are:', end=' ')
        for itemList in parList:
            disp(itemList)

def print_range_86(parRange):
    if len(parRange)==0:
        print('The range is empty.')
    else:
        print('The range items are:', end=' ')
        for itemRange in parRange:
            print('{}'.format(itemRange), end=' ')

# if __name__=='__main__': main_8_6()

# --------------------------------------
# chapter 9 lesson 1
# Creating a Class

def main_9_1():
    # the code for chapter 9 lesson 1
    donald = Duck_9_1() # creating the donald obj from the class
    donald.quack() # call the function sound from donald obj
    donald.move() # call the function move from the object donald

class Duck_9_1:
    sound = 'Quack quack.'
    movement = 'Walks like a duck.'

    def quack(self):
        # define the quack method in the this class
        # using the self to refer to the object
        print(self.sound)
    
    def move(self):
        # define the method for moving in this class
        print(self.movement)

# if __name__=='__main__': main_9_1()

# --------------------------------------
# chapter 9 lesson 2
# Constructing an Object

class Animal_9_2:
    # for the old branch ch9les2_exclusiveParameters we use the below code
    #  def __init__(self, type, name, sound):
    #     self._type = type
    #     self._name = name
    #     self._sound = sound

    # for the new branch ch9les2_kwargsParameters we use the below code
    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'default_type'
        self._name = kwargs['name'] if 'name' in kwargs else 'default_name'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'default_sound'

    def type(self):
        return self._type
    
    def name(self):
        return self._name

    def sound(self):
        return self._sound

def print_animal_9_6(parAnimal):
    # print the object variables
    if not isinstance(parAnimal, Animal_9_2):
        raise TypeError('print_animal(): requires an Animal')
    print('The {} is named "{}" and says {}'.format(parAnimal.type(), parAnimal.name(), parAnimal.sound()))

def main_9_2():
    # the code for the chapter 9 lesson 2
    # a0 = Animal_9_2('kitten', 'fluffy', 'rwar') # excl. parameters
    a0 = Animal_9_2(type='kitten', name='fluffy', sound='rwar')
    # a1 = Animal_9_2('duck', 'donald', 'quack') # excl. parameters
    a1 = Animal_9_2(type='duck', name='donald', sound='quack')
    print_animal_9_6(a0)
    print_animal_9_6(a1)
    print_animal_9_6(Animal_9_2(type='velociraptor', name='veronica', sound='hello'))
    print_animal_9_6(Animal_9_2())

# if __name__=='__main__': main_9_2()

# --------------------------------------
# chapter 9 lesson 3
# Class Methods

class Animal_9_3:

    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'default_type'
        self._name = kwargs['name'] if 'name' in kwargs else 'default_name'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'default_sound'

    def type(self, t=None):
        # this is a getter-setter
        if t:
            self._type=t
        return self._type
    
    def name(self, n=None):
        # another getter setter
        if n:
            self._name=n
        return self._name

    def sound(self, s=None):
        if s:
            self._sound=s
        return self._sound
    
    def __str__(self):
        return f'The {self.type()} is named "{self.name()}" and says {self.sound()}'

def print_animal_9_3(parAnimal):
    # print the object variables
    if not isinstance(parAnimal, Animal_9_3):
        raise TypeError('print_animal(): requires an Animal')
    print('The {} is named "{}" and says {}'.format(parAnimal.type(), parAnimal.name(), parAnimal.sound()))

def main_9_3():
    # the code for the chapter 9 lesson 3
    a0 = Animal_9_3(type='kitten', name='fluffy', sound='rwar')
    a1 = Animal_9_3(type='duck', name='donald', sound='quack')
    a0.sound('bark')
    # print_animal_9_3(a0)
    print(a0)
    # print_animal_9_3(a1)
    print(a1)


# if __name__=='__main__': main_9_3()


# --------------------------------------
# chapter 9 lesson 4
# Object Data

class Animal_9_4:

    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'default_type'
        self._name = kwargs['name'] if 'name' in kwargs else 'default_name'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'default_sound'

    def type(self, t=None):
        # this is a getter-setter
        if t:
            self._type=t
        return self._type
    
    def name(self, n=None):
        # another getter setter
        if n:
            self._name=n
        return self._name

    def sound(self, s=None):
        if s:
            self._sound=s
        return self._sound

    def __str__(self):
        return f'The {self.type()} is named "{self.name()}" and says {self.sound()}'

def print_animal_9_4(parAnimal):
    # print the object variables
    if not isinstance(parAnimal, Animal_9_4):
        raise TypeError('print_animal(): requires an Animal')
    print('The {} is named "{}" and says {}'.format(parAnimal.type(), parAnimal.name(), parAnimal.sound()))

def main_9_4():
    # the code for the chapter 9 lesson 4
    a0 = Animal_9_4(type='kitten', name='fluffy', sound='rwar')
    a1 = Animal_9_4(type='duck', name='donald', sound='quack')
    a0.sound('bark')
    # print_animal_9_4(a0)
    print(a0)
    # print_animal_9_4(a1)
    print(a1)
    
# if __name__=='__main__': main_9_4()

# --------------------------------------
# chapter 9 lesson 5
# Inheritance

class Animal_9_5:
    def __init__(self, **kwargs):
        # initialize the object variables if they exist
        if 'type' in kwargs:
            self._type=kwargs['type']
        if 'name' in kwargs:
            self._name=kwargs['name']
        if 'sound' in kwargs:
            self._sound=kwargs['sound']

    def type(self, t=None):
        # this is a getter-setter
        if t:
            self._type=t
        try: 
            return self._type
        except AttributeError:
            return None

    
    def name(self, n=None):
        # another getter setter
        if n:
            self._name=n
        try:
            return self._name
        except AttributeError:
            return None

    def sound(self, s=None):
        if s:
            self._sound=s
        try: 
            return self._sound
        except AttributeError:
            return None

    def __str__(self):
        return f'The {self.type()} is named "{self.name()}" and says {self.sound()}'

class Duck_9_5(Animal_9_5):
    def __init__(self, **kwargs):
        self._type='duck'
        if 'type' in kwargs:
            del kwargs['type']
        super().__init__(**kwargs)

class Kitten_9_5(Animal_9_5):
    def __init__(self, **kwargs):
        self._type='kitten'
        if 'type' in kwargs:
            del kwargs['type']
        super().__init__(**kwargs)

    def kill(self, pTarget):
        """pTarget (as string) = the target that this (self) kitten will kill, ex: 'human', 'mouse', etc."""
        print(f'{self.name()} will now kill all {pTarget}!')

def main_9_5():
    # the code for the chapter 9 lesson 5
    a0 = Kitten_9_5(name='fluffy', sound='rwar')
    a1 = Duck_9_5(name='donald', sound='quack')
    a0.sound('bark')
    print(a0)
    print(a1)
    a0.kill("human")
    
# if __name__=='__main__': main_9_5()

# --------------------------------------
# chapter 9 lesson 6
# Iterator Objects

class inclusive_range:
    # this class will work as a RANGE but with including the last number (i.e. inclusive_range(5) will return 0 to 5 and not 0 to 4)
    def __init__(self, *args):
        numargs=len(args)
        self._start=0
        self._step=1

        if numargs<1:
            raise TypeError(f'Expected at least one argument, got {numargs}')
        elif numargs==1:
            self._stop=args[0]
        elif numargs==2:
            (self._start, self._stop)=args
        elif numargs==3:
            (self._start, self._stop, self._step)=args
        else:
            raise TypeError('expected at most 3 arguments, got {}'.format(numargs))

        self._next=self._start

    def __iter__(self):
        # this makes this class an ITERATOR
        return self
    
    def __next__(self):
        # needed for the iterator
        if self._next>self._stop:
            raise StopIteration
        else:
            _r=self._next
            self._next+=self._step
            return _r

def main_9_6():
    for n in inclusive_range(0, 25, 5):
        print(n, end =' ')
    print()

# if __name__=='__main__': main_9_6()



# --------------------------------------
# chapter 10 lesson 1
# Handling Exceptions

def main_10_1():
    # code for chapter 10 lesson 1
    try:
        x = 5/0
    except ValueError:
        print('I caught a ValueError')
    # except ZeroDivisionError:
    #     print('You can\'t divide by zero.')
    except:
        print('general error: {}'.format(sys.exc_info()[1]))
    else:
        print('Good job! x = {}'.format(x))

# if __name__=='__main__': main_10_1()


# --------------------------------------
# chapter 10 lesson 2
# Reporting Errors

def inclusive_range_10_2(*args):
    # this inclusive range will be constructed as a generator not an iterator
    """The function is returning a range of numbers, including the last number.
    param debug=True/False, [start], stop, [step]
    """
    if isinstance(args[0], bool):
        if args[0]==True:
            print('_____debug: running in debug mode.')
        elif args[0]==False:
            print('_____debug: running in non-debug mode.')
    else:
        raise TypeError('The first argument of the function needs to be True or False. True for debug info.')

    numargs=len(args)
    start = 0
    step = 1

    # initialize parameters
    if numargs<=1:
        raise TypeError('This function needs between 2 and 4 arguments. The function recieved {} arguments'.format(numargs))
    if numargs==2:
        stop=args[1]
        if args[0]==True:
            print('_____debug: <<initializing parameters>> stop={}'.format(stop))
    elif numargs==3:
        start=args[1]
        stop=args[2]
        if args[0]==True:
            print('_____debug: <<initializing parameters>> start={}, stop=={}'.format(start, stop))
    elif numargs==4:
        start=args[1]
        stop=args[2]
        step=args[3]
        if args[0]==True:
            print('_____debug: <<initializing parameters>> start={}, stop={}, step={}'.format(start, stop, step))
    else:
        raise TypeError('This function needs between 2 and 4 arguments. The function recieved {} arguments.'.format(numargs))

    # generator
    i = start
    while i<=stop:
        yield i
        i+=step

def main_10_2():
    # the start code of the lesson 2 in chapter 10
    try:
        x=inclusive_range_10_2(False, 0, 5, 1, 5) # OPT1 --- no arguments; should raise an error
        for i in x:
            print(i, end=' ')
        print()
    except TypeError as e:
        print('ERROR: >>> {}'.format(e))

# if __name__=='__main__': main_10_2()

# --------------------------------------
# chapter 11 lesson 1
# Overview of String Objects

def main_11_1():
    s = MyString('Hello World!')
    print(s)

class MyString(str):
    def __str__(self):
        return self[::-1]

# if __name__=='__main__': main_11_1()

# --------------------------------------
# chapter 11 lesson 2
# Common String Methods

def main_11_2():
    # the code for lesson 2 in chapter 11
    print('Hello, World!') # initial code
    print('Hello, World!'.upper()) # using the upper method on a string
    print('Hello, World!'.lower()) # using the lower method on string
    print('Hello, World!'.capitalize()) # capitalizing a string
    print('hello, world!'.title()) # convert a string to title case
    print('Hello, World!'.swapcase()) # some fun :)
    print('Hello, World! ß'.casefold()) # removes all case distinctions, even in unicode

    # diffferent object IDs = strings are imutable
    s1 = 'Hello, World!'
    s2 = s1.upper()
    print(id(s1))
    print(id(s2))

    # using the concatenate operator
    s1_2='Hello, World!'
    s2_2='This is another string.'
    s3_2='this is string 1' ' ' 'this is string 2'
    print(s1_2 + ' ' + s2_2)
    print(s3_2)
# if __name__=='__main__': main_11_2()

# --------------------------------------
# chapter 11 lesson 3
# Formatting Strings

def main_11_3():
    # code for the lesson 3 in chapter 11
    x=42 * 747 * 1000
    y=73
    print('the number is {0} {1}'.format(x, y)) # format with 2 numbers
    print('the number is {:,.3f}'.format(x)) # customer format of numbers
    print(f'the number is {x:,}')

# if __name__=='__main__': main_11_3()

# --------------------------------------
# chapter 11 lesson 4
# Splitting and joining

def main_11_4():
    # code for the chapter 11 lesson 4
    s = 'This is a long string with a bunch of words in it.'
    # print(s.split())
    l = s.split()
    s2 = ' '.join(l) 
    print(s2)

# if __name__=='__main__': main_11_4()

# --------------------------------------
# chapter 12 lesson 1
# Opening Files

def main_12_1():
    # code for the chapter 12 lesson 1
    f = open('lines.txt')
    for line in f:
        print(line.rstrip()) # rstrip - deletes the new lines at the end of a line
        # print(line) # line without \n CrLf stripping

# if __name__=='__main__': main_12_1()

# --------------------------------------
# chapter 12 lesson 2
# Text vs. Binary Files

def main_12_2():
    # code for the lesson 2 in chapter 12
    x = 'String\n' # line feed / carriage return
    print(x)

if __name__=='__main__': main_12_2()

