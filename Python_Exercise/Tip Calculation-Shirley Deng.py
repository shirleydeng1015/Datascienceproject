#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 21:12:39 2018

@author: shirleydeng
"""

price = float(input("Enter the price of a meal:"))

tip = price * 0.16
total = price + tip

print("A 16% tip would be ", tip)
print("The total including tip would be ", total)