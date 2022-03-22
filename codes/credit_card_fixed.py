#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 16:11:31 2022

@author: aldonunes
"""

balance = 3926
annualInterestRate = 0.2
pay = 10
nb = None
ub = None

while True:
    nb = balance
    for i in range(12):
        ub = nb - pay
        nb = ub + (annualInterestRate / 12.0) * ub
    
    if nb <= 0:
        break
    
    pay += 10


print('Lowest Payment:', pay)