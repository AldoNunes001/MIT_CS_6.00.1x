#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 16:19:24 2022

@author: aldonunes
"""

for elt in map(abs, [1, -2, 3, -4]):
    print(elt)

print()

l1 = [1, 28, 36]
l2 = [2, 57, 9 ]
for elt in map(min, l1, l2):
    print(elt)
