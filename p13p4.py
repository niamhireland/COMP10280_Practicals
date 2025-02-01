#implement the program that illustrates scoping in Python from the lectures 
#from Page 12 of the notes on Lecture 15, the section on “Scoping”.

def f(x):
    """Function that adds 1 to its argument and prints it out"""
    print('In function f:')
    x += 1
    y = 1
    print('x is', x)
    print('y is', y)
    print('z is', z)
    return x

x, y, z = 5, 10, 15
print('Before function f:')
print('x is', x)
print('y is', y)
print('z is', z)

z = f(x)
print('After function f:')
print('x is', x)
print('y is', y)
print('z is', z)