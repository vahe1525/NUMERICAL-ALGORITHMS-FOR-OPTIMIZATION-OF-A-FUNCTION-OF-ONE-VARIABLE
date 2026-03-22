import sympy as sp
import math
import matplotlib.pyplot as plt
import numpy as np

class ObjectiveFunction:
    
    def __call__(self, x):
        return 0.25 * (x**4) + (x**2) - 8 * x + 12


class GoldenSectionSearch:
       
    def __init__(self, func, a, b, epsilon):
        self.func = func
        self.a = a
        self.b = b
        self.epsilon = epsilon
        self.phi = (math.sqrt(5) - 1) / 2
        self.iterations = 0
        self.min_x = None
        self.min_y = None
        self.history = [] # Hook 1: History
    
    def search(self):
        x1 = self.b - self.phi * (self.b - self.a)
        x2 = self.a + self.phi * (self.b - self.a)
        
        y1 = self.func(x1)
        y2 = self.func(x2)
        
        while (self.b - self.a) >= self.epsilon:
            self.history.append((self.a + self.b) / 2) # Hook 2: Capture midpoint
            if y1 < y2:
                self.b = x2
                x2 = x1
                y2 = y1
                x1 = self.b - self.phi * (self.b - self.a)
                y1 = self.func(x1)
            else:
                self.a = x1
                x1 = x2
                y1 = y2
                x2 = self.a + self.phi * (self.b - self.a)
                y2 = self.func(x2)
            
            self.iterations += 1
        
        self.min_x = (self.a + self.b) / 2
        self.min_y = self.func(self.min_x)
        self.history.append(self.min_x)

        return self.min_x, self.min_y
    
def plot_result(func, a, b, history, min_x, min_y, title):
    x_vals = np.linspace(a, b, 100)
    y_vals = [func(x) for x in x_vals]
    plt.plot(x_vals, y_vals, label='f(x)', color='black', alpha=0.5)
    
    # Plot steps
    hx = history
    hy = [func(x) for x in hx]
    plt.scatter(hx, hy, color='green', s=20, label='Algorithm Steps')
    plt.plot(hx, hy, color='green', alpha=0.3)
    
    # Mark minimum
    plt.scatter(min_x, min_y, color='blue', marker='x', s=100, label='Found Minimum')
    
    plt.title(title)
    plt.legend()
    plt.show()

def calculate_analytical_minimum():
    x = sp.Symbol('x')
    f = 0.25 * x**4 + x**2 - 8*x + 12
    
    f_prime = sp.diff(f, x)
    all_roots = sp.solve(f_prime, x)
    
    real_roots = [root.evalf() for root in all_roots if sp.im(root) == 0]
    real_min_x = real_roots[0]
    
    return real_min_x


def main():
    objective_func = ObjectiveFunction()
    a_start, b_start = 0.0, 2.0
    
    golden = GoldenSectionSearch(
        func=objective_func,
        a=a_start,
        b=b_start,
        epsilon=0.5
    )
    
    min_x, min_y = golden.search()
    
    plot_result(objective_func, a_start, b_start, golden.history, min_x, min_y, "Golden Section Search")
    
    analytical_min_x = calculate_analytical_minimum()
    loss = abs(min_x - analytical_min_x)
    
    print(f"Analytic Minimum X: {analytical_min_x}")
    print(f"Loss is {loss}")
    print(f"The Golden Section min x is {min_x:.5f} and min y is {min_y:.5f}")


if __name__ == "__main__":
    main()