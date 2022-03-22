#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 15:51:01 2022

@author: aldonunes
"""

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
ub = None

for i in range(12):
    p = balance * monthlyPaymentRate
    
    ub = balance - p
    balance = ub + (annualInterestRate / 12.0) * ub
        
    
        
print(f'Month {i+1} Remaining balance: {balance:.2f}')