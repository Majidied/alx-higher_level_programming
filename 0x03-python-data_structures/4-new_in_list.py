#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = list.copy(my_list)
    if idx < 0 and idx > lenght(new_list):
        return new_list
    else:
        new_list[idx] = element
        return new_list
