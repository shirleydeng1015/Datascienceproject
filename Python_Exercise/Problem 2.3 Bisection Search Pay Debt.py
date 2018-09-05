#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 00:33:07 2017

@author: shirleydeng
"""
balance = 320000
annualInterestRate = 0.20

initBalance = balance
monthlyInterestRate = annualInterestRate/12.0
lowest = balance/12.0
highest = (balance*((1.0 + monthlyInterestRate)**12))/12.0
adding = 0.01
minPay = (lowest+highest)/2.0
month = 0

def calculatepayment(month, balance, minPay, monthlyInterestRate):
    
    while month <= 11:
        unpaidBalance = balance - minPay
        balance = unpaidBalance + (monthlyInterestRate*unpaidBalance)
        month += 1
        
    return balance

while abs(balance) >= adding:
    balance = initBalance
    month = 0
    balance = calculatepayment(month, balance, minPay, monthlyInterestRate)
    if balance > 0:
        lowest = minPay
    else:
        highest = minPay
    minPay = (lowest + highest)/2.0
    
minPay = round(minPay,2)
print("Lowest Payment: " + str(minPay))    
            