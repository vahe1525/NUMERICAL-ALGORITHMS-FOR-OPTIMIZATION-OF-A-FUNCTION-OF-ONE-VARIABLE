import math
from Brute_force_function_minimazing import BruteForceMinimizer
from Golden_Section import GoldenSectionSearch
from Method_of_Dichotomy import DichotomousSearch
import sympy as sp

 

class ObjectiveFunctionExam:
    def __call__(self, x):
        return ((x-2) ** 2) - 3 * math.log(x)


def main():
    func_exam = ObjectiveFunctionExam()

    a = 0.5
    b = 4
    eps = 0.5
    n = 7
    delta = 0.125

    golden = GoldenSectionSearch(
        func=func_exam,
        a=0.0,
        b=2.0,
        epsilon=0.5
    )

    dichotomous = DichotomousSearch(
        func=func_exam, 
        a=0.0, 
        b=2.0, 
        epsilon=0.5, 
        delta=0.1
    )

    brute_force = BruteForceMinimizer(func_exam, a, b, eps)

    min_x, min_y = golden.search()
    # min_x, min_y = dichotomous.search()
    # min_x, min_y = brute_force.find_minimum()


    analytical_x = calculate_analytical_minimum()
    loss = abs(min_x - analytical_x)
    
    print(f"Analytic Minimum X: {analytical_x:.6f}")
    print(f"ALG Min X:  {min_x:.6f}")
    print(f"ALG Min Y:  {min_y:.6f}")
    print(f"Loss:               {loss:.6f}")

    


def calculate_analytical_minimum():
    x = sp.Symbol('x')
    
    f = (x - 2)**2 - 3 * sp.log(x)
    
    f_prime = sp.diff(f, x)
    
    all_roots = sp.solve(f_prime, x)
    
    real_roots = [root.evalf() for root in all_roots if sp.im(root) == 0]
    
    interval_min, interval_max = 0.5, 4
    valid_roots = [r for r in real_roots if interval_min <= r <= interval_max]
    
    return valid_roots[0] if valid_roots else real_roots[0]

main()