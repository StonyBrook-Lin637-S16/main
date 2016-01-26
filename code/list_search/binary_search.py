#!/usr/bin/env python
# encoding: utf-8


def binary_search(search_list, item, start=None, end=None):
    """
    Binary search algorithm with optional subrange of a list.

    This algorithm is more efficient but only works for sorted lists!

    Arguments:
    search_list -- list to be searched
    item        -- item we are looking for
    start       -- start index of search range
    end         -- end index of search range
    """
    # instantiate default values
    if start is None:
        start = 0

    if end is None:
        end = len(search_list) - 1

    # if a range is given by user, make sure it's sane
    if start < 0 or end > len(search_list) - 1:
        print("Indices outside valid range for given list")

    # if the range is ill-defined it cannot contain the item
    if end < start:
        return False

    # find middle of the current range
    middle = start + (end - start)/2

    # Case 1: our item is to the left of the item at the midpoint
    if item < search_list[middle]:
        return binary_search(search_list, item, start, middle - 1)
    # Case 2: our item is to the right of the item at the midpoint
    elif item > search_list[middle]:
        return binary_search(search_list, item, middle + 1, end)
    # Case 3: we found our item, return its index
    elif item == search_list[middle]:
        return middle
