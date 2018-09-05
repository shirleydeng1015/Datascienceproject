#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 11:03:52 2017

@author: shirleydeng
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    oddTup = ()
    n = 0
    while n < len(aTup):
        oddTup += (aTup[n],)
        n += 2
    return oddTup

testList = [5, -20, 40, -45]
def dividefive(n):
    n = n//5
    n = abs(n)
    return n
    
def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
animals['e'] = ['cat']


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    
    result = None
    biggestvalue = 0
    for key in aDict.keys():
        if len(aDict[key]) >= biggestvalue:
            result = key
            biggestvalue = len(aDict[key])
    return result
    


def fib_efficient(n,d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1,d) + fib_efficient(n-2,d)
        d[n] = ans
        return ans

d = {1:1, 2:2}
print(fib_efficient(6, d))

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    