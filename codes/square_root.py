#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 17:10:38 2022

@author: aldonunes
"""

# Square root

x = 54
epsilon = 0.01
num_guesses = 0
low = 1.0
high = x
ans = (high + low) / 2.0

while abs(ans**2 - x) >= epsilon:
    print(f"low = {low}  high = {high}  ans = {ans}")
    num_guesses += 1
    
    if ans**2 < x:
        low = ans 
    else:
        high = ans 
        
    ans = (high + low) / 2.0
    
print(f"num_guesses = {num_guesses}")
print(f"{ans} is close to square root of {x}")
