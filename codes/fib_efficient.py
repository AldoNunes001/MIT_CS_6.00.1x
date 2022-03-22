#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 16:08:31 2022

@author: aldonunes
"""

def fib_efficient(n, d):
    
    if n in d:
        return d[n]
    
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans
    

d = {1:1, 2:2}
print(fib_efficient(5, d))
        