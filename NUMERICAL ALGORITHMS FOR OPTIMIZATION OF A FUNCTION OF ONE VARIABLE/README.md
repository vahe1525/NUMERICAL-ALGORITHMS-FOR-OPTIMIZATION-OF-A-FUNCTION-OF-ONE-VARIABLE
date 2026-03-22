# Numerical Optimization of a Function of One Variable

This project contains three classic algorithms used to find the **minimum value** of a mathematical function within a specific range $[a, b]$. It also includes a visualization tool to see exactly how each algorithm "walks" toward the solution.

---

## 1. Brute Force Search (Exhaustive Search)

### How it works:
Imagine you are looking for the lowest point in a valley, and you decide to take small, equal-sized steps from one end to the other. At every step, you check your height. After reaching the end, you simply remember which step was the lowest.
*   **The Process:** It divides the interval into many tiny segments (based on your `epsilon` precision) and checks every single point.

### Pros and Cons:
*   **Pros:** Very simple to understand and impossible to "miss" the minimum if your steps are small enough.
*   **Cons:** Very slow. If you want high precision, it has to check thousands of points, even if they are clearly nowhere near the minimum.

---

## 2. Method of Dichotomy (Interval Halving)

### How it works:
This is a "divide and conquer" strategy. Instead of checking every point, it looks at the middle of the current range.
*   **The Process:** 
    1. Pick the midpoint.
    2. Test two points very close to that midpoint ($mid - delta$ and $mid + delta$).
    3. Compare the values: if the left point is lower, the minimum must be in the left half. If the right is lower, it's in the right half.
    4. Throw away the "bad" half and repeat until the remaining space is tiny.

### Pros and Cons:
*   **Pros:** Much faster than Brute Force because it cuts the search area in half every time.
*   **Cons:** Requires two function calculations per step. It's efficient, but not the most "elegant" math-wise.

---

## 3. Golden Section Search

### How it works:
This is the most "sophisticated" of the three. It is similar to the Dichotomy method but uses the **Golden Ratio** ($\approx 0.618$) to pick the test points.
*   **The Process:** By placing the test points at specific "Golden" distances, the algorithm can **reuse** one of the points from the previous step. This means it only needs to calculate the function value *once* per iteration after the first step.

### Pros and Cons:
*   **Pros:** The most efficient method for these types of problems. It converges very quickly and saves computational power by reusing data.
*   **Cons:** Slightly more complex to code because of the Golden Ratio math.

---

## How to Run the Demo

The main file `NUMERICAL_ALGORITHMS_FOR_OPTIMIZATION_OF_A_FUNCTION_OF_ONE_VARIABLE.py` is set up to solve the function:
**$f(x) = (x-2)^2 - 3 \ln(x)$**

### Requirements:
*   Python 3.x
*   Matplotlib (`pip install matplotlib`)
*   NumPy (`pip install numpy`)
*   SymPy (`pip install sympy`)

### Running the program:
Simply run the main script:
```bash
python NUMERICAL_ALGORITHMS_FOR_OPTIMIZATION_OF_A_FUNCTION_OF_ONE_VARIABLE.py
```
A window will pop up for each algorithm showing:
- **Black Line:** The actual function.
- **Colored Dots:** The steps the algorithm took.
- **Black Star:** Where the algorithm started.
- **Blue X:** The final minimum point found.

---

## Summary Comparison

| Algorithm | Speed | Efficiency | Complexity |
| :--- | :--- | :--- | :--- |
| **Brute Force** | Slow | Low | Very Simple |
| **Dichotomy** | Fast | Medium | Simple |
| **Golden Section**| Very Fast | High | Moderate |
