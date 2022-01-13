import numpy as np

def peak_detect(data, multiplication_factor):
    above_this_range_is_a_peak = np.median(data) + multiplication_factor * data.std()
    return np.array( [i for i, x in enumerate(data) if x > above_this_range_is_a_peak] )