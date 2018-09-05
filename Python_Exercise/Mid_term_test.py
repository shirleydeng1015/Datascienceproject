def jumpAndBackpedal(isMyNumber):
    '''
    isMyNumber: Procedure that hides a secret number. 
     It takes as a parameter one number and returns:
     *  -1 if the number is less than the secret number
     *  0 if the number is equal to the secret number
     *  1 if the number is greater than the secret number
    returns: integer, the secret number
    ''' 
    # if isMyNumber(guess) == 0:
    #     return guess
    # foundNumber = False
    # while not foundNumber:
    #     sign = isMyNumber(guess)
    #     if sign == -1:
    #         guess += 1
    #     elif sign == -1:
    #         guess -= 1
            
    # return guess
    guess = 1        
    while True:
        sign = isMyNumber(guess)
        if sign == -1:
            guess += 1
        elif sign == 1:
            guess -= 1
        else:
            return guess

def isMyNumber(guess):
    correct = 90
    if guess == correct:
        return 0
    elif guess < correct:
        return -1
    elif guess > correct:
        return 1


# print(jumpAndBackpedal(isMyNumber))

aList = ["apple", "cat", "dog", "banana"]
def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    newlist = []
    for string in aList:
        if len(string) < 4:
            newlist.append(string)
    return newlist

# print(lessThan4(aList))


aDict = {"a":1, "b":2, "c":3,"d":2,"e":4,"r":1}
target = 1

# print(aDict.get(1))
# print(aDict.keys())
# print(aDict.values())
# print(len(aDict))
def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    newlist = []
    for key, value in aDict.items():
        if value == target:
            newlist.append(key)
    return sorted(newlist)

#print(keysWithValue(aDict, target))
t = (5, (1,2), [[1],[9]])
def max_val(t): 
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """ 
    # newlist = []
    local_max = None
    for items in t:
        if type(items) == int:
            if local_max == None:
                local_max = items
            elif local_max < items:
                local_max = items
        
        else:
            list_max = max_val(items)
            if local_max == None or list_max > local_max:
                local_max = list_max

    return local_max



#print(max_val(t))





# def max_val(t): 
#     """ t, tuple or list
#         Each element of t is either an int, a tuple, or a list
#         No tuple or list is empty
#         Returns the maximum int in t or (recursively) in an element of t """ 
#     newlist = []
#     for items in t:
#         if type(items) == int:
#             newlist.append(items)
#         elif type(items) == tuple:
#             for i in items:
#                 newlist.append(i)
#         elif type(items) == list:
#             for i in items:

#                 if type(i) == list:
#                     for k in i:
#                         newlist.append(k)
#                 else:
#                     newlist.append(i)

#     return max(newlist)
def f(s):
    return 'a' in s

def run_satisfiesF(L, satisfiesF):
    pass

L = ['a', 'b', 'a', 'c', 'e', 'a']
# print(f(L))

def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
        """
    
    i = 0
    while i in range(len(L)):
        if f(L[i]):
            i += 1
        else:                
            L.remove(L[i])
        print(L)
         
    return len(L)


print(satisfiesF(L))
print(L)






run_satisfiesF(L, satisfiesF)


























