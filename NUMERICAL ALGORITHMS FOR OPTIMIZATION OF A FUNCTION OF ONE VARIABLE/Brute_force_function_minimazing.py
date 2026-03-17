import sympy as sp

class ObjectiveFunction:
    def __call__(self, x):
        return 0.25 * (x**4) + (x**2) - 8 * x + 12

class BruteForceMinimizer:
    def __init__(self, func, a, b, eps):
        self.func = func
        self.a = a
        self.b = b
        self.eps = eps
      
    def find_minimum(self):
        n = int((self.b - self.a) / self.eps)
        h = (self.b - self.a) / n
        
        current_x = self.a
        
        for i in range(n + 1):
            y = self.func(current_x)
            
            if y < self.min_y:
                self.min_y = y
                self.min_x = current_x
            
            current_x += h
            
        return self.min_x, self.min_y

def calculate_analytical_minimum():
    x = sp.Symbol('x')
    f = 0.25 * x**4 + x**2 - 8*x + 12
    f_prime = sp.diff(f, x)
    real_roots = [root.evalf() for root in sp.solve(f_prime, x) if sp.im(root) == 0]
    return real_roots[0]

def main():
    a, b, eps = 0.0, 2.0, 0.5
    
    objective = ObjectiveFunction()
    brute_force = BruteForceMinimizer(objective, a, b, eps)
    
    min_x, min_y = brute_force.find_minimum()
    
    analytical_x = calculate_analytical_minimum()
    loss = abs(min_x - analytical_x)
    
    print(f"Analytic Minimum X: {analytical_x:.6f}")
    print(f"Brute Force Min X:  {min_x:.6f}")
    print(f"Brute Force Min Y:  {min_y:.6f}")
    print(f"Loss:               {loss:.6f}")

if __name__ == "__main__":
    main()