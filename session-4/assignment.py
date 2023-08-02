# Lists in Python
def create_list(n):
    '''
        Task: Create a list of n integers starting from 0.
    '''
    n_integers=[x for x in range(0,n)]

    result = n_integers
    return result

def find_element_in_list(lst, element):
    '''
        Task: Check if element is in lst and return a boolean result.
    '''
    if element in lst:
        return True
    else:
        return False
    
# List comprehensions
def generate_square_list(n):
    '''
        Task: Generate a list of squares of integers from 0 to n using list comprehension.
    '''
    listofsquares = [x**2 for x in range (0,(n+1))]

    result = listofsquares
    return result
    
# List methods
def add_element(lst, element):
    '''
        Task: Add element to the end of lst.
    '''

    lst.append(element)
    result = lst
    return result

def remove_element(lst, element):
    '''
        Task: Remove element from lst.
    '''
    
    lst.remove(element)
    result = lst
    return result

# Dictionaries
def create_dict(keys, values):
    '''
        Task: Create a dictionary from keys and values.
    '''
    f = {keys[i]:values[i] for i in range(0,len(keys))}
    result = f
    return result

def get_value_from_key(dct, key):
    '''
        Task: Get value of key from dct.
    '''

    thevalue = dct[key]
    result = thevalue
    return result

# Dictionary comprehensions
def generate_dict(n):
    '''
        Task: Generate a dictionary where keys are integers from 0 to n and values are their squares.
    '''
    dictionarysquares  = {x:x**2 for x in range(0, n+1)}
    result = dictionarysquares
    return result

# Dictionary methods
def get_keys(dct):
    '''
        Task: Get all keys from dct.
    '''
    return list(dct.keys())

def get_values(dct):
    '''
        Task: Get all values from dct.
    '''

    return list(dct.values()) 

# Negative indexing
def get_last_element(lst):
    '''
        Task: Get the last element from lst using negative indexing.
    '''
    lastelement = lst[-1]
    result = lastelement
    return result

# List slicing
def get_slice(lst, start, end):
    '''
        Task: Get a slice from lst from index start to end.
    '''
    sliceoflist = lst[start:end:1]
    result = sliceoflist
    return result

# For loop
def count_elements(lst):
    '''
        Task: Count the number of elements in lst using a for loop.
    '''
    counter = 0
    for element in lst:
        counter+=1
    result = counter
    return result

# Range function
def create_range(start, end):
    '''
        Task: Create a range of integers from start to end.
    '''
    return list(range(start,end))


# If else
def check_greater(a, b):
    '''
        Task: Check if a is greater than b.
    '''
    if a>b:
        return True
    else:
        return False 
        

# If else with logical operators
def check_in_range(n, start, end):
    '''
        Task: Check if n is in the range between start and end.
    '''
    if n in range(start,end):
        return True
    else:
        return False
        

