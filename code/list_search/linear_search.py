#!/usr/bin/env python
# encoding: utf-8


def linear_search(search_list, searched_item):
    """Search trough list from left to right"""
    for i in range(len(search_list)):
        if searched_item == search_list[i]:
            print("Item found at index " + str(i))
            return i
    return False
