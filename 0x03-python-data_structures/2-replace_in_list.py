#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    Replaces an element of a list at a specific position
    ...

    Parameters
    ----------
    my_list : list
        The list of elements
    idx : integer
        The given position
    element : the new element

    Return:
        The original list if idx is negative or
        if idx out of range (> len(my_list))
    """

    if idx < 0 or idx > lenght(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list
