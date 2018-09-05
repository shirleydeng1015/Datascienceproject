#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 17:41:44 2017

@author: shirleydeng
"""
aDict = {'B': [15], 'u': [10, 15, 5, 2, 6]}

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    result = 0 
    for key in aDict.keys():
        result += len(aDict[key])
    return result