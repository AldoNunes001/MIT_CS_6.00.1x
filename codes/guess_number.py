#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 18:56:21 2022

@author: aldonunes
"""

# secret number
low = 0
high = 100
guess = int((high + low) / 2)

print("Please think of a number between 0 and 100!")

while True:
    print(f"Is your secret number {guess}?", end='')
    ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to "
                "indicate the guess is too low. Enter 'c' to indicate I guessed"
                " correctly. ")
    
    if ans == 'h':
        high = guess 
    elif ans == 'l':
        low = guess 
    elif ans == 'c':
        print(f"Game over. Your secret number was: {guess}")
        break 
    else:
        print("Sorry, I did not understand your input.")
    
    guess = int((high + low) / 2)
    
            
        
        
    
    