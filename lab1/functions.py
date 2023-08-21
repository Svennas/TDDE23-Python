def find_root():
    """ Prints the approximation of the square root of a given number """
    print("This program tries to find the square root of a number ")
    x = int(input("Enter a number: "))
    guess = x / 2
    for i in range(5):
        guess = (guess + x / guess) / 2
        print(guess)

def table():
    """ Prints the multiplication table of a given number """
    print("This program prints out a multiplication table.")
    x = int(input("Enter a number: "))
    for i in range(10):
        answer = x * i
        print("{} * {} = {}".format(i, x, answer))
        
    
def div_by_three(x):
    answer = x / 3
    print("{} divided by 3 equals {}".format(x, answer))
    
    return answer % 1.0 == 0.0
    
    
def max2(x, y):
    if x >= y: return x    
    else: return y
    
    
def max3(x, y, z):
    
    if max2(x, y) == x:
        if max2(x, z) == x: return x
        else: return z
    else:
        if max2(y, z) == y: return y
        else: return z