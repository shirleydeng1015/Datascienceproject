#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 12:59:09 2018

@author: shirleydeng
"""

def checkpalindrome(name):
    n = 0
    ispalindrome = True 
    newname = ''
    while n < len(name):
        idx = len(name)-n-1
        if n == 0:
            newname += (name[idx].upper())
        else:
            newname += (name[idx].lower())
        if ispalindrome:
            ispalindrome = (name[n].lower() == name[idx].lower())
        n += 1
    if ispalindrome:
        print('Palindrome!')
    
    else: 
        print(newname)
        

name = input('Enter you name? ')
print(checkpalindrome(name))