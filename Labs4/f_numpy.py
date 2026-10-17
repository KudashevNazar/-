import numpy as np

def array_stats(numbers):
    arr = np.array(numbers)
    return {"mean": float(np.mean(arr)), "max": int(np.max(arr)), "min": int(np.min(arr))}