import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    sample_mean = np.mean(x)
    sample_var = 0
    for i in x:
        sample_var += (sample_mean - i) ** 2
    sample_var /= (len(x)-1)
    std = sample_var ** 0.5
    return {
        "variance": float(sample_var),
        "standard_deviation": float(std)
    }