#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 17:25:41 2018

@author: shirleydeng
"""
#3-1. Pig Latin Translator

#originname = input('Enter your name: ')
#names = originname.split()
#for name in names:
#    newname = name[1:len(name)]+name[0]
#    newname = newname[0].upper() + newname[1:].lower()
#    newname = newname+str('ay')
#    print(newname, ' ', end = '')


#3-2. Matrix Inverter

#originmatrix = input('Give me four numbers and seperate them in space: ')
#orimat = originmatrix.split()
#a = float(orimat[0])
#b = float(orimat[1])
#c = float(orimat[2])
#d = float(orimat[3])
#a1 = (1/(a*d-b*c))*d
#b1 = (1/(a*d-b*c))*(-b)
#c1 = (1/(a*d-b*c))*(-c)
#d1 = (1/(a*d-b*c))*a
#print('matrix: ', '(','(', a,',',b,')',',','(',c,',',d,')',')')
#
#print('inverse: ', '(','(', a1,',',b1,')',',','(',c1,',',d1,')',')')

### 3-3. Create a to-do list program using a dictionary of lists

todolist = {}
while True:
    userorder = input("Prompt: What would you like to do? \n" + 
                      "Enter 'add' if you want to add tast, \n" + 
                      "Enter 'get' to get the task, \n" +
                      "Enter 'quit' to quit the to-do-list.\n" +
                      "Your order: ")
    if userorder == 'add':
        day = input('Prompt: What day? ')
        task = input("Prompt: What would you like to ad to " + day + "'s to-do list?")
        todolist[day] = task
    elif userorder == 'get':
        check = input('Prompt: What day?')
        if check in todolist:
            print('Response: You have to', todolist[check])
        else:
            print("Response: You don't have task that day. ")
    elif userorder == 'quit':
        print('Response: Ending program. Thank you for using the to-do list!')
        break


### 3-4. Fibonacci Series



### 3-5. Pascal's Triangle
