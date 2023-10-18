def unit(x):
    x = x % 1000
    x = x % 100
    x = x % 10
    return x


def ten(x):
    x = x % 1000
    x = x % 100
    x = x // 10
    return x


def swap_unit_ten(x):
    a = x // 100 * 100
    b = unit(x) * 10
    c = ten(x)
    return a + b + c


def power(x, y):
    if (y == 0): return 1
    
    i = 1
    while i < y:
        x *= x
        i += 1
        
    return x
    
    
def sum_first(x):
    sum = 0
    for i in range(x):
        sum += i
        
    sum += x
    return sum


import numbers

def isnumber(x):
    return isinstance(x, numbers.Number)


def sum_numbers(list):
    sum = 0
    for x in list:
        if (isnumber(x)):
            sum += x    
    return sum


def find_letter(l, list):
    for i in list:
        if (i == l):
            return True
    return False


def remove_vowels(list):
    vowels = ["a", "e", "i", "o", "u", "y"]
    cons = []
    for i in list:
        if not (find_letter(i, vowels)):
           cons.append(i)
    return cons