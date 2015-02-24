#!/usr/bin/env python
# encoding: utf-8


def prob_base(w, grammar):
    return grammar.get(w, 0)


def prob_compose(s, t):
    return s * t
