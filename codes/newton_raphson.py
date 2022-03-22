#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 10:45:14 2022

@author: aldonunes
"""

# Newton-Raphson guesses

epsilon = 0.01
y = 27.0
guess = y / 2.0
g = y / 3.0
numGuesses = 0
ng = 0

while abs(guess * guess -y) >= epsilon:
    numGuesses += 1
    guess = guess - (((guess ** 2) - y) / (2 * guess))
    
print('numGuesses = ' + str(numGuesses))
print('Square root of ' + str(y) + ' is about ' + str(guess))
print()

# Cube root
while abs(g * g * g - y) >= epsilon:
    ng += 1
    g = g - (((g ** 3) - y) / (3 * (g ** 2)))
    
print('ng = ' + str(ng))
print('Cube root of ' + str(y) + ' is about ' + str(g))    
