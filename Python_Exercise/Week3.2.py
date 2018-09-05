#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 01:30:23 2018

@author: shirleydeng
"""

### 3-4. Fibonacci Series

#x = int(input("Enter a number: "))
#n = 1
#m = 1
#print(n, ' ', end = '')
#while m <= x:
#    print(str(m), ' ', end = '')
#    n,m = m, n+m
#   
#    

import math
    
### 3-5. Pascal's Triangle
def coefficient(n, k):
    return int(math.factorial(n) / (math.factorial(k) * math.factorial(n - k)))
    
n = int(input("Input a number: "))
for k in range(n):
    print(coefficient(n-1, k), ' ', end = '')