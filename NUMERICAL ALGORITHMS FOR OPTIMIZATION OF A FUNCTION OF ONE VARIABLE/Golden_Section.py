import sympy as sp
import math

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
    
    def search(self):
        x1 = self.b - self.phi * (self.b - self.a)
        x2 = self.a + self.phi * (self.b - self.a)
        
        y1 = self.func(x1)
        y2 = self.func(x2)
        
        while (self.b - self.a) >= self.epsilon:
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

        return self.min_x, self.min_y
    
       
    
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
    
    golden = GoldenSectionSearch(
        func=objective_func,
        a=0.0,
        b=2.0,
        epsilon=0.5
    )
    
    min_x, min_y = golden.search()
    
    analytical_min_x = calculate_analytical_minimum()
    loss = abs(min_x - analytical_min_x)
    
    print(f"Analytic Minimum X: {analytical_min_x}")
    print(f"Loss is {loss}")
    print(f"The Golden Section min x is {min_x:.5f} and min y is {min_y:.5f}")


if __name__ == "__main__":
    main()