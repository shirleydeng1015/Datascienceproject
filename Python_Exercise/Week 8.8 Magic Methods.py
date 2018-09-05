#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 23:17:02 2018

@author: shirleydeng
"""

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        
    def __eq__(self, other):
        if self.value == other.value:
            return True
        else:
            return False
    def __lt__(self, other):
        if self.value < other.value:
            return True
        else:
            return False
        
    def __gt__(self, other):
        if self.value > other.value:
            return True
        else:
            return False
    def __repr__(self):
        return "%i of %s" % (self. value, self.suit)
        
cards = []
for suit in ["♠", "♥", "♦", "♣"]:
    for value in range(1, 14):
        cards.append(Card(value, suit))
           
print(cards)

from random import shuffle
shuffle(cards)
print(cards[:5])
        
class Vector:
    def __init__(self, numbers):
        self.__numbers = numbers
        
    @property
    def numbers(self):
        return self.__numbers
    
    def dot(self, other):
        values = []
        if len(self.__numbers) != len(other.numbers):
            return "cannot Mulitply Different Size Vectors"
        for x in range(len(self.__numbers)):
            this_num = self.__numbers[x]
            other_num = other.numbers[x]
            values.append(this_num * other_num)
        return sum(values)
    def __mul__(self, other):
        return self.dot(other)
    
a = Vector([1, 10, 4])
b = Vector([2, -1, 5])
print(a*b)
print(a.dot(b))