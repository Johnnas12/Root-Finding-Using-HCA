from math import *

# The code implements the Bisection Method for root finding in Python.
def f(x):
    """Define the function whose root we want to find."""
    return x**2 - x - 2

def validate_interval(a, b):
    """Check if the function has opposite signs at a and b."""
    if f(a) * f(b) > 0:
        print('Error: The function must have opposite signs at a and b.')
        return False
    elif f(a) * f(b) == 0:
        if f(a) == 0:
            print(f'The root is: {a}')
        if f(b) == 0:
            print(f'The root is: {b}')
        return False
    else:
        print("✅ The values are suitable for the Bisection Method.")
        return True

def bisection_method(a, b, max_iterations):
    """Perform the bisection method."""
    for i in range(1, max_iterations + 1):
        c = (a + b) / 2
        print(f'Iteration {i}: a={a}, b={b}, c={c}, f(c)={f(c)}')
        
        if f(c) == 0:
            print(f'Exact root found at c = {c}')
            return c
        
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    print(f'Approximate root after {max_iterations} iterations is: {c}')
    return c

def main():
    print('Enter the values of a and b such that f(a) * f(b) < 0')
    a = float(input('Enter a: '))
    b = float(input('Enter b: '))
    
    if validate_interval(a, b):
        n = int(input('Enter the number of iterations: '))
        root = bisection_method(a, b, n)
        print(f'\n✅ Final estimated root: {root}')

if __name__ == "__main__":
    main()