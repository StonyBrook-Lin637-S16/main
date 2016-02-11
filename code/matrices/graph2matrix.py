#!/usr/bin/env python
# -*- coding: utf-8 -*-


def graph2matrix(graph):
    """
    Converts graph into adjacency matrix, represented as list of lists

    Arguments:
    graph -- list of the form
             [ [list of vertices],
               [list of edges encoded as (source,target,label) tuples]
             ]
    """
    # inititalize empty matrix with a nested list comprehension
    graph_size = range(len(graph[0]))
    matrix = [['' for i in graph_size] for i in graph_size]

    # fill matrix
    for edge in graph[1]:
        source_index = graph[0].index(edge[0])
        target_index = graph[0].index(edge[1])
        edge_label = edge[2]
        matrix[source_index][target_index] = edge_label
    return matrix
