#!/usr/bin/env python
# encoding: utf-8


def grammatical_base(w, grammar):
        return w in grammar


def grammatical_compose(s, t):
        return s & t
