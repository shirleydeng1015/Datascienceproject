#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 23:40:44 2017

@author: shirleydeng
"""

balance = 3329
annualInterestRate = 0.20
monthlyInterestRate = annualInterestRate/12
minPay = 10
month = 0
def calculatebalance(month, balance, minPay, monthlyInterestRate):
    while month <= 11:
        unpaidBalance = balance - minPay
        balance = unpaidBalance + monthlyInterestRate*unpaidBalance
        month += 1
    return balance
#while calculatebalance(month, balance, minPay, monthlyInterestRate) > 0:
 #   minPay += 10
  #  month = 0
   # calculatebalance(month, balance, minPay, monthlyInterestRate)
#print("Lowest Payment: " +str(minPay))


def newcalbalance(month, balance, minPay, monthlyInterestRate):
    while month <= 11:
        
        unpaidBalance = balance - minPay
        newbalance = unpaidBalance + monthlyInterestRate*unpaidBalance
        balance = newbalance
        month += 1
    return balance

while newcalbalance(month, balance, minPay, monthlyInterestRate) > 0 and month <= 11:
    minPay += 10
    newcalbalance(month, balance, minPay, monthlyInterestRate)
print ("Lowest Payment: " + str(minPay))