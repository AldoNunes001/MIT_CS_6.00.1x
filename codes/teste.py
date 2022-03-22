#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 09:55:07 2022

@author: aldonunes
"""

# Import the math module
import math

# Built the function
def polysum(n, s):
    
    area = (0.25 * n * s**2) / (math.tan(math.pi/n))
    peri = n * s
    
    suma = area + peri**2
    
    return float(f'{suma:.4f}')


print(polysum(89, 20))        