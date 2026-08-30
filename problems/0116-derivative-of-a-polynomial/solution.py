import math
def poly_term_derivative(c: float, x: float, n: float) -> float:
    # Your code here
    return c*n*(math.pow(x,n-1))
    pass