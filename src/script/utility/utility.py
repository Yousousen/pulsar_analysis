import numpy as np

def short_list(lst):
    """
    Returns a string that is a short representation of list lst; useful for long lists.
    """
    if len(lst) >= 4:
        return f"{lst[0]},\t{lst[1]},\t...\t,{lst[-1]},\t{lst[-2]}"
    return lst

def elements_containing_string(search_query, lst):
    """
    This function exists to prevent repeatingly writing the (unreadable) list
    comprehension it returns to find the elements of the list that contain the
    search_query.
    """
    return [x for x in lst if x.lower().find(search_query.strip().lower()) != -1]

def contains_substring(str, sub_str):
    """
    More readable syntax for checking if a string contains a substring.
    """
    return str.lower().find(sub_str.strip().lower()) != -1

def slice_string_at_char(str, char):
    """
    Returns a list of strings splitted on char.
    """
    return str.split(char)

def get_metadata_item(metadata, item):
    return slice_string_at_char(elements_containing_string(item, metadata)[0], '=')[1]
    
def err_period(frequencies):
    frequency_mean = np.mean(frequencies)
    frequency_std = np.std(frequencies)
    error = (frequency_std)/(frequency_mean**2)
    return error

def period_and_error(frequencies):
    return 1 / (mean := np.mean(frequencies)), np.std(frequencies) / mean**2