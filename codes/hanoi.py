#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 18:51:27 2022

@author: aldonunes
"""
count = 0
def printMove(fr, to):
    print(f'move from {fr} to {to}')
    
def towers(n, fr, to, spare, count):
    if n == 1:
        printMove(fr, to)
        return count + 1
    else:
        towers(n-1, fr, spare, to, count)
        towers(1, fr, to, spare, count)
        towers(n-1, spare, to, fr, count)
        
count = towers(50, 'P1', 'P2', 'P3', count)
print(count)
