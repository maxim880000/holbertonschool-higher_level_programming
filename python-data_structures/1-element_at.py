#!/usr/bin/python3
# retrieves an element from a list
def element_at(my_list, idx):
    # conditions index sup long list
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
