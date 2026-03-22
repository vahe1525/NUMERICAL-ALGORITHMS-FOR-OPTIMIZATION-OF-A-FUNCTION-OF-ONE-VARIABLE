import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

class ObjectiveFunction:
    def __call__(self, x):
        return 0.25 * (x**4) + (x**2) - 8 * x + 12

class DichotomousSearch:
    def __init__(self, func, a, b, epsilon, delta):
        self.func = func
        self.a = a
        self.b = b
        self.epsilon = epsilon
        self.delta = delta  
        self.iterations = 0
        self.min_x = None
        self.min_y = None
        self.history = [] # Hook 1: History

    def search(self):
        a_curr, b_curr = self.a, self.b
        
        while (b_curr - a_curr) >= self.epsilon:
            midpoint = (a_curr + b_curr) / 2
            self.history.append(midpoint) # Hook 2: Capture steps
            
            x1 = midpoint - self.delta
            x2 = midpoint + self.delta
            
            y1 = self.func(x1)
            y2 = self.func(x2)
            
            if y1 < y2:
                b_curr = x2
            else:
                a_curr = x1
                
            self.iterations += 1

        self.min_x = (a_curr + b_curr) / 2
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
    plt.scatter(hx, hy, color='orange', s=20, label='Algorithm Steps')
    plt.plot(hx, hy, color='orange', alpha=0.3)
    
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
    return real_roots[0]

def main():
    objective = ObjectiveFunction()
    a_start, b_start = 0.0, 2.0
    
    dichotomous = DichotomousSearch(
        func=objective, 
        a=a_start, 
        b=b_start, 
        epsilon=0.5, 
        delta=0.1
    )
    
    min_x, min_y = dichotomous.search()
    
    plot_result(objective, a_start, b_start, dichotomous.history, min_x, min_y, "Dichotomous Search")
    
    analytical_x = calculate_analytical_minimum()
    loss = abs(min_x - analytical_x)
    
    print(f"Analytic Minimum X: {analytical_x:.6f}")
    print(f"Dichotomous Min X:  {min_x:.6f}")
    print(f"Dichotomous Min Y:  {min_y:.6f}")
    print(f"Loss:               {loss:.6f}")

if __name__ == "__main__":
    main()