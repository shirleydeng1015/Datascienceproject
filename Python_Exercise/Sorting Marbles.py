#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 20:32:10 2018

@author: shirleydeng
"""

class MarblesBoard:
    from collections import deque
    def __init__(self, marbles):
    
        '''
        In a particular board game, there are N spaces in a row, numbered 0 through N - 1 from left to right. 
        There are also N marbles, numbered 0 through N - 1, initially placed in some arbitrary order.
        '''
        self.input = list(marbles)
       
    def switch(self):
        '''Switch the marbles in positions 0 and 1.'''
        self.input = [self.input[1], self.input[0]] + self.input[2:]        
    
    def rotate(self):
        '''Move the marble in position 0 to position N - 1, 
        and move all other marbles one space to the left (one index lower). 
        The objective is to arrange the marbles in order, with each marble i in position i.
        '''
        self.input = self.input[1:] + self.input[:1]
    
    def is_solved(self):
        for i in range(len(self.input)-1):
            if self.input[i] >= self.input[i+1]:
                return False
            
        return True
    
    def is_head_the_largest(self):
        for e in self.input:
            if e > self.input[0]:
                return False
        return True
                        
    def __str__(self):
        return  ' '.join(str(e) for e in self.input)
    
    def __repr__():
        return 
    

class Solver:
    
    def __init__(self, marble_board):
        self.marble_board = marble_board
    
    def solve(self):
        step = 0
        while self.marble_board.is_solved() is False:
            if self.marble_board.input[1] < self.marble_board.input[0] and not self.marble_board.is_head_the_largest():
                self.marble_board.switch()
            else:                
                self.marble_board.rotate()
                
            print(self.marble_board)
            step += 1
            
        print('Total step is', step)
            
    
board = MarblesBoard((3,6,7,4,1,0,8,2,5))
MarblesGame = Solver(board)
MarblesGame.solve()
