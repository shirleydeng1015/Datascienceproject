#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 22:30:08 2017

@author: shirleydeng
"""

'''
Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.
balance - the outstanding balance on the credit card
annualInterestRate - the annual interest rate as decimal
monthlyPaymentRate - minimum monthly payment rate as a decimal
'''
balance = 5000
monthlyPaymentRate = 2
annualInterestRate = 18

m = 1 
while m <= 12:
    
    minimumPayment = round(monthlyPaymentRate * balance/100,2)
    interestPayment = round((balance-minimumPayment)*annualInterestRate/12/100,2)
    unpaidBalance = round((balance-minimumPayment),2)
    newbalance = round((unpaidBalance+interestPayment),2)
    print("Month "+str(m))
    print("Minimum Payment at Month " +str(m) +" is " +str(minimumPayment))
    print("Interest Payment at Month " +str(m) +" is " + str(interestPayment))
    print("New balance is " + str(newbalance))

    balance = newbalance
    m += 1
print("Remaining balance: " +str(balance))
       