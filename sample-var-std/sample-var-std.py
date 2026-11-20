import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    x = np.asarray(x,dtype="float")
    mean = np.mean(x)
    variance = 0.0
    for item in x:
        variance += (mean - item) ** 2
    variance = float(variance / (x.shape[0] - 1))
    return {
        "variance": (variance),
        "standard_deviation": variance ** 0.5
    }