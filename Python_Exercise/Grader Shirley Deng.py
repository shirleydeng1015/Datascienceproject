#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 20:37:02 2017

@author: shirleydeng
"""

import math
def polysum(n,s):
    sum = 0.25*n*s**2/(math.tan(math.pi/n))
    square = (s*n)**2
    return round(sum+square,4)
    