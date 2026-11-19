from collections import Counter,defaultdict
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    mean = float(np.mean(x).item())
    median = float(np.median(x).item())
    min_index, max_node = 0, defaultdict(int)
    max_value = 0

    for i in range(len(x)):
        max_node[x[i]] += 1
        if max_node[x[i]] > max_value:
            max_value = max_node[x[i]]
            min_index = i
    return {
        "mean":mean,
        "median": median,
        "mode": float(x[min_index])
    }
        