import numpy as np
def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    # Your code here
    [a,b,c,d] = np.array(matrix).flatten()
    det = a*d-b*c
    if det!=0:
        a_inv = (1/det)*np.array([[d,-b],[-c,a]])     

        return a_inv
    else:
        return None
