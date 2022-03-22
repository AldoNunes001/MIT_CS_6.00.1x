#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 20:11:47 2022

@author: aldonunes
"""

# Float to binary

x = float(input("Enter a decimal number between 0 and 1: "))

p = 0
while (x * (2 ** p)) % 1 != 0:
    print(f"Remainder = {(2**p)*x - int((2**p)*x)}")
    p += 1
    
num = int(x * (2 ** p))

result = ''
if num == 0:
    result = '0'
    
while num > 0:
    result = str(num % 2) + result
    num = num // 2
    
for i in range(p - len(result)):
    result = '0' + result 
    
tes1 = result[0:-p] # Esse nao serve de nada. Retorna uma string vazia
tes2 = result[-p:] # Esse retorna o proprio result

result = tes1 + '.' + tes2 
print('The binary representation of the decimal ' + str(x))
print(result)

