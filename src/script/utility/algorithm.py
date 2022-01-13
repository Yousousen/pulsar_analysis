import numpy as np

def peak_detect(data, multiplication_factor, binsize):
    '''
    DEPRICATED, in favor of Eleni's improvements on the find_peak function.
    '''
    above_this_range_is_a_peak = np.median(data) + multiplication_factor * data.std()
    # We now want to create bins in which we take the peak of in a specific bin.
    everything_that_is_above = np.array( [i for i, x in enumerate(data) if x > above_this_range_is_a_peak] )
    chunks = [everything_that_is_above[x:x+binsize] for x in range(0, len(everything_that_is_above), binsize)]
    return [ max(x) for x in chunks ]

def n_max_intensities(intensities, n):
    """
    To be used in conjunction with n_max_frequencies
    """
    return list( reversed( sorted( intensities ) ) )[:n]

def n_max_frequencies(frequencies, intensities, max_intensities):
    """
    To be used in conjunction with n_max_intensities and after the 'peaks' have been detected.
    Note that frequencies must be a numpy array.
    """
    return frequencies[ [np.where( intensities == x )[0][0]  for x in max_intensities] ]