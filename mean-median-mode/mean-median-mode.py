from collections import Counter, defaultdict
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    x = np.asarray(x,dtype="float")
    mean = np.mean(x).item()
    median = np.median(x).item()

    min_index, max_value = 0,0
    state_holder = defaultdict(int)

    for idx,item in enumerate(x):
        state_holder[item] += 1
        if state_holder[item] > max_value:
            max_value = state_holder[item]
            min_index = idx
    return {
        "mean":mean,
        "median":median,
        "mode":float(x[min_index])
    }