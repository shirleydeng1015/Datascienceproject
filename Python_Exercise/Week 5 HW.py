#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 21:17:23 2018

@author: shirleydeng
"""

#def sum_digits(x):
#    sum_digit = 0
#    x = abs(x)
#    while x > 0:
#        sum_digit += x % 10
#        x = int(x / 10)
#    return sum_digit
#
#def diff_sum_digits(x):
#    return x - sum_digits(x)
#
#def wraps_diff_sum_digits(x):
#    x = abs(x)
#    while x > 9:
#        x = diff_sum_digits(x)
#    return x 
#
#
#print(wraps_diff_sum_digits(54321))    

#total = 0
#
#def process_order(x_list):
#    global total
#    item = x_list.pop()
#    itemtotal = item[2]*item[1]
#    print('You filled an order for', item[1], item[0], 'for a total of $', itemtotal)
#    total += itemtotal
#    
#
#x = [("oranges", 4, 3.22),("gummy bears",1,1.99),("sour bites", 3, 2.33), ("antacid", 1, 5.33)]
#while(len(x)>0):
#    process_order(x)
#print("Total price: ", total)

while True:
    try:     
        x = float(input("Enter a number: "))
        print("The reciprocal of your number is", 1/x)
        break 
    except ValueError:
        print("You did not enter a valid number.")
    except ZeroDivisionError:
        print("Zero does not have a reciprocal")
        break
    except:
        print("something else went wrong.")
