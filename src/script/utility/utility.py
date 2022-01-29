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
    return slice_string_at_char(elements_containing_string(item, metadata)[0], "=")[1]


def err_period(frequencies):
    frequency_mean = np.mean(frequencies)
    frequency_std = np.std(frequencies)
    error = (frequency_std) / (frequency_mean ** 2)
    return error


def period_and_error(frequencies):
    return 1 / (mean := np.mean(frequencies)), np.std(frequencies) / mean ** 2


def find_period_in_index(period, dt):
    period_in_index = int(round(period // dt))
    return period_in_index


def stacking(pulsar_data, period_in_index, nbins):
    # create a dictionary with all the stacks
    stack_dict = dict()
    i = 0
    while i <= nbins:
        stack_dict[f"stack{i // period_in_index}"] = np.array(
            pulsar_data[i : i + period_in_index]
        )
        i += period_in_index

    stack = np.zeros(
        period_in_index
    )  # initializing with zeroes to get the correct stack size.
    for key, val in stack_dict.items():
        if (
            length := len(val)
        ) != period_in_index:  # This should only happen happen at the end.
            continue
        else:
            stack += val
    return stack
