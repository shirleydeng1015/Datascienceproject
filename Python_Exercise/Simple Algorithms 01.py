#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 16:58:41 2017

@author: shirleydeng
"""
guess = 0
l = -1
h = 101

print("Please think of a number between 0 and 100!")
while guess in range (l, h):
    guess = int((l + h)/2)
    print("Is your secret number " + str(guess)+ "?")
    tips=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. :")
    if tips == 'l':
        l = guess
    elif tips == 'h':
        h = guess + 1
    elif tips == 'c':
        print("Game over. Your secret number was: "+ str(guess))
        break
    else:
        print("Sorry, I did not understand your input.")



    