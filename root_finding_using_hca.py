import matplotlib.pyplot as plt
import numpy as np
from math import *
# Hill Climbing Algorithm for Root Finding
def f(x):
    return x**2 - x - 2

def hill_climbing(f, x_start, step_size, max_iterations, tolerance):
    x = x_start
    history = [x] 

    for i in range(max_iterations):
        current_value = abs(f(x))
        next_x1 = x + step_size
        next_x2 = x - step_size

        value1 = abs(f(next_x1))
        value2 = abs(f(next_x2))

        print(f"Iteration {i+1}: x = {x}, f(x) = {f(x)}")

        if value1 < current_value and value1 < value2:
            x = next_x1
        elif value2 < current_value:
            x = next_x2
        else:
            break

        history.append(x)

        if abs(f(x)) < tolerance:
            break

    return x, history

# Inputs
x_start = float(input("Enter starting guess: "))
step_size = float(input("Enter step size (e.g., 0.01): "))
max_iter = int(input("Enter maximum number of iterations: "))
tolerance = float(input("Enter tolerance (e.g.,0.0000005): "))


root, path = hill_climbing(f, x_start, step_size, max_iter, tolerance)
print(f"\nEstimated root: {root}")

# Plotting
x_vals = np.linspace(min(path) - 1, max(path) + 1, 400)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals, label="f(x)", color='blue')
plt.axhline(0, color='gray', linestyle='--')
plt.scatter(path, [f(x) for x in path], color='red', label='Steps')
plt.plot(path, [f(x) for x in path], color='orange', linestyle='--', label='Path')
plt.title("Hill Climbing Root Finding Visualization")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()