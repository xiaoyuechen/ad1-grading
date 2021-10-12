#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 01:58:27 2021

@author: Daniel Brown and Yashas Koppa Ramesh

Insertion sort implementation. Sorts an array A in place.
"""

def inssort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j-1
        while i > -1 and a[i] > key:
            a[i+1] = a[i]
            i = i-1
        a[i+1] = key
