#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 15:30:35 2022

@author: aldonunes
"""

# Cube root

cube = 27
epsilon = 0.01
guess = 0.0
increment = 0.0001
num_guesses = 0

while abs(guess**3 - cube) >= epsilon and guess <= cube:
    guess += increment
    num_guesses += 1
    
print(f"num_guesses = {num_guesses}")

if abs(guess**3 - cube) >= epsilon:
    print("Failed on cube root of {cube}")
else:
    print(f"{guess} is close to the cube root of {cube}")
    