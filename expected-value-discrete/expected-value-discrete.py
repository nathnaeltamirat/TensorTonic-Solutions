import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    # Write code here
    x = np.asarray(x,dtype="float")
    p = np.asarray(p,dtype="float")
    summation = 0
    for xi,pi in zip(x,p):
        summation += (xi * pi)
    return summation