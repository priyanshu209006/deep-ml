import numpy as np
import math

def svd_2x2(a: np.ndarray) -> tuple:
    """
    Compute SVD of a 2x2 matrix using one Jacobi rotation.
    """

    b = a.T @ a

    # Jacobi rotation angle
    if b[0, 0] == b[1, 1]:
        theta = np.pi / 4
    else:
        theta = 0.5 * np.arctan2(
            2 * b[0, 1],
            b[0, 0] - b[1, 1]
        )

    # Eigenvector matrix of A^T A
    v = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]
    ])

    # Diagonalize A^T A
    d = v.T @ b @ v

    lambda_1 = d[0, 0]
    lambda_2 = d[1, 1]

    # Singular values MUST stay paired with V's columns
    s_2 = np.array([
        np.sqrt(max(lambda_1, 0)),
        np.sqrt(max(lambda_2, 0))
    ])

    s = np.diag(s_2)

    # Compute U
    u = a @ v @ np.linalg.inv(s)

    return u, s_2, v.T