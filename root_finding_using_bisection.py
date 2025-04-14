from math import *
import matplotlib.pyplot as plt
import numpy as np

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
    """Perform the bisection method and return the root and midpoints."""
    midpoints = []

    for i in range(1, max_iterations + 1):
        c = (a + b) / 2
        midpoints.append(c)
        print(f'Iteration {i}: a={a}, b={b}, c={c}, f(c)={f(c)}')

        if f(c) == 0:
            print(f'Exact root found at c = {c}')
            break

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    print(f'Approximate root after {max_iterations} iterations is: {c}')
    return c, midpoints

def plot_function_and_bisection(a, b, midpoints):
    """Plot the function and midpoints during the bisection process."""
    x_vals = np.linspace(a - 1, b + 1, 400)
    y_vals = f(x_vals)

    plt.figure(figsize=(10, 6))
    plt.axhline(0, color='gray', linestyle='--')
    plt.plot(x_vals, y_vals, label='f(x)', color='blue')

    # Plot midpoints
    for i, c in enumerate(midpoints):
        plt.plot(c, f(c), 'ro')
        plt.text(c, f(c), f'{i+1}', fontsize=9, ha='right', va='bottom')

    plt.title('Bisection Method Visualization')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    print('Enter the values of a and b such that f(a) * f(b) < 0')
    a = float(input('Enter a: '))
    b = float(input('Enter b: '))
    
    if validate_interval(a, b):
        n = int(input('Enter the number of iterations: '))
        root, midpoints = bisection_method(a, b, n)
        print(f'\n✅ Final estimated root: {root}')
        plot_function_and_bisection(a, b, midpoints)

if __name__ == "__main__":
    main()
