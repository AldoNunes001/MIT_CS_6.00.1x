#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 16:11:31 2022

@author: aldonunes
"""

balance = 999999
annualInterestRate = 0.18
month = annualInterestRate / 12
nb = None
ub = None
upper = (balance * (1 + month)**12) / 12.0
lower = balance / 12.0
pay = (upper + lower) / 2.0

while True:
    nb = balance
    for i in range(12):
        ub = nb - pay
        nb = ub + (annualInterestRate / 12.0) * ub
    
    if nb < 0.01:
        upper = pay
        pay = (upper + lower) / 2
    
    elif nb >= 0.02:
        lower = pay
        pay = (upper + lower) / 2
    
    else:
        break

pay = round(pay, 2)

print('Lowest Payment:', pay)