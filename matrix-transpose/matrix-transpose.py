import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    A = np.asarray(A)
    n, m = A.shape
    A_transpose = np.zeros((m,n))
    for i in range(n):
        for j in range(m):
            A_transpose[j][i] = A[i][j]
    return A_transpose

    
