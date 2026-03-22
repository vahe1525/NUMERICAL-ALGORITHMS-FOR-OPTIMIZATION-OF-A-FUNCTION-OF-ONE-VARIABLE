import math
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
from Brute_force_function_minimazing import BruteForceMinimizer
from Golden_Section import GoldenSectionSearch
from Method_of_Dichotomy import DichotomousSearch

class ObjectiveFunctionExam:
    def __call__(self, x):
        return ((x-2) ** 2) - 3 * math.log(x)

def plot_optimization(func, a, b, history, min_x, min_y, title, color):
    # Plot the objective function curve
    x_vals = np.linspace(a, b, 500)
    y_vals = [func(x) for x in x_vals]
    plt.plot(x_vals, y_vals, label='f(x)', color='black', alpha=0.5)
    
    # Plot algorithm steps (the 'history')
    hx = history
    hy = [func(x) for x in hx]
    plt.scatter(hx, hy, color=color, s=25, label='Algorithm Steps', edgecolors='white', linewidths=0.5)
    plt.plot(hx, hy, color=color, alpha=0.3)
    
    # Mark the starting point and final minimum
    plt.scatter(hx[0], hy[0], color='black', marker='*', s=150, label='Start')
    plt.scatter(min_x, min_y, color='blue', marker='X', s=150, label='Found Min')
    
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

def calculate_analytical_minimum():
    x = sp.Symbol('x')
    f = (x - 2)**2 - 3 * sp.log(x)
    f_prime = sp.diff(f, x)
    all_roots = sp.solve(f_prime, x)
    real_roots = [root.evalf() for root in all_roots if sp.im(root) == 0]
    interval_min, interval_max = 0.5, 4.0
    valid_roots = [r for r in real_roots if interval_min <= r <= interval_max]
    return valid_roots[0] if valid_roots else real_roots[0]

def main():
    func_exam = ObjectiveFunctionExam()
    a, b, eps = 0.5, 4.0, 0.5 
    delta = 0.125

    print(f"--- Running Optimization Demo on f(x) = (x-2)^2 - 3ln(x) ---")
    analytical_x = calculate_analytical_minimum()
    print(f"Analytic Minimum X: {analytical_x:.6f}\n")

    # Golden Section Search
    print("Running Golden Section Search...")
    golden = GoldenSectionSearch(func_exam, a, b, eps)
    min_x_g, min_y_g = golden.search()
    print(f"Result: x={min_x_g:.5f}, y={min_y_g:.5f}, steps={len(golden.history)}")
    plot_optimization(func_exam, a, b, golden.history, min_x_g, min_y_g, "Golden Section Search", "green")

    # Dichotomous Search
    print("\nRunning Dichotomous Search...")
    dichotomous = DichotomousSearch(func_exam, a, b, eps, delta=delta)
    min_x_d, min_y_d = dichotomous.search()
    print(f"Result: x={min_x_d:.5f}, y={min_y_d:.5f}, steps={len(dichotomous.history)}")
    plot_optimization(func_exam, a, b, dichotomous.history, min_x_d, min_y_d, "Dichotomous Search", "orange")

    # Brute Force Search
    print("\nRunning Brute Force Search...")
    brute_force = BruteForceMinimizer(func_exam, a, b, eps)
    min_x_b, min_y_b = brute_force.find_minimum()
    print(f"Result: x={min_x_b:.5f}, y={min_y_b:.5f}, steps={len(brute_force.history)}")
    plot_optimization(func_exam, a, b, brute_force.history, min_x_b, min_y_b, "Brute Force Search", "red")

if __name__ == "__main__":
    main()
