#!/usr/bin/env python
# encoding: utf-8


def ngram_set_base(w):
    return set([w])


def ngram_set_compose(s, t):
    return s.union(t)
