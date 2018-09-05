#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 16:28:51 2018

@author: shirleydeng
"""

'''
This is for the exercise of debugging
'''
def rem(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the remainder when x is divided by a.
    """
    if x == a:
        return 0
    elif x < a:
        return x
    else:
        return rem(x-a, a)
        
def f(n):
   """
   n: integer, n >= 0.
   """
   if n == 0 or n == 1:
      return n
   else:
      return n * f(n-1)

def fancy_divide(numbers,index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        print("-1")
    else:
        print("1")
    finally:
        print("0")
        
def fancy_divide_test(numbers, index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
        print('try execute')
    except IndexError:
        
        fancy_divide_test(numbers, len(numbers) - 1)
        
        print("indexerror")
    except ZeroDivisionError:
        print("zerodevisionerror")
    else:
        print("else")
    finally:
        print("finally")
        
def fancy_divide_test2(numbers, index):
    try:
        try:
            denom = numbers[index]
            for i in range(len(numbers)):
                numbers[i] /= denom
            print('try execute')
        except IndexError:
            fancy_divide_test2(numbers, len(numbers) - 1)
            print('except execute')
        else:
            print("else")
        finally:
            print("finally")
    except ZeroDivisionError:
        print("-2")
        