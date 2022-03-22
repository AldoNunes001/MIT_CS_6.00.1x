#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 20:04:00 2022

@author: aldonunes
"""

num = -4

if num < 0:
    isNeg = True 
    num = abs(num)
else:
    isNeg = False
    
result = ''

# The magic
while num > 0:
    result = str(num%2) + result
    num = num // 2
    
if isNeg:
    result = '-' + result
    
print(result)
    