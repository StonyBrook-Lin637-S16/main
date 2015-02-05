#!/usr/bin/env python
# encoding: utf-8


def linear_search(search_list, search_item):
    """Search trough list from left to right"""
    for i in range(len(search_list)):
        if search_item == search_list[i]:
            print("Item found at index " + str(i))
            return i
    return False
