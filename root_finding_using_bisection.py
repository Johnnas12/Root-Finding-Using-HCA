#  Exprimenting Root Finding using Bisection Method
from math import * 

def f(x):
    # Define the function for which we want to find the root
    return x**2 - x - 2

print('Enter the values of a and b such that f(a) * f(b)< 0')
a = float(input('Enter a: '))
b = float(input('Enter b: '))

# Check if the function has opposite signs at a and b
if f(a) * f(b) > 0:
    print('The function must have opposite signs at a and b.') 
elif f(a) * f(b) == 0:
    if f(a) == 0:
        print(f'The root is: {a}')
    if f(b) == 0:
        print(f'The root is: {b}')
else:
    print("The values are suitable for bisection method")

n = int(input('Enter the number of iterations: '))
i = 1
while i <= n:
    c = (a + b) / 2
    print('iteration:', i, 'a=', a, 'b=', b, 'c=', c, 'f(c)=', f(c))
    if f(a) * f(c) > 0:
        a = c
    if f(a) * f(c) == 0:
        print(f'The root is: {c}')
        break
    if f(a) * f(c) < 0:
        b = c
    i += 1

print('The root is:', c)