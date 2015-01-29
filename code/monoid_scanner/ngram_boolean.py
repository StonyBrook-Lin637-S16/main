#!/usr/bin/env python
# encoding: utf-8


def boolean_base(w, grammar):
        return w in grammar


def boolean_compose(s, t):
        return s & t
