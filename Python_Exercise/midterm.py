#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 13:22:46 2018

@author: shirleydeng

"""
#from collections import Counter
#
#tweets_list = ["This is great! RT @fake_user: Can you believe this http://some-link.com",
#         "It's the refs! RT @dubsfan: Boo the refs and stuff wargarbal",
#         "That's right RT @ladodgers: The dodgers are destined to win the west!",
#         "RT @sportball: That sporting event was not cool",
#         "This is just a tweet about things @person, how could you",
#         "RT @ladodgers: The season is looking great!",
#         "RT @dubsfan: I can't believe it!",
#         "I can't believe it either! RT @dubsfan: I can't believe it"]
#user_name = []
#for tweets in tweets_list:
##    print(tweets)
#    for word in tweets.split():
#        if word.startswith("@"):
#            user_name.append(word[:-1])
#    
##print(user_name)
#retweet = Counter(user_name)
#print(retweet)

#
#def count_retweets_by_username(tweet_list):
#    """ (list of tweets) -> dict of {username: int}
#    Returns a dictionary in which each key is a username that was 
#    retweeted in tweet_list and each value is the total number of times this 
#    username was retweeted.
#    """
#    from collections import Counter
#    user_name = []
#    for tweets in tweets_list:
#    #    print(tweets)
#        for word in tweets.split():
#            if word.startswith("@"):
#                user_name.append(word[:-1])
#    
#    #print(user_name)
#    retweet = dict(Counter(user_name))
#    return retweet

#def display(deposits, top, bottom, left, right):
#    lookup = {}
#    s = ''
#    for t in deposits:
#        lookup[(t[0], t[1])] = t[2]
#        
#    for i in range(top, bottom):
#        for j in range(left, right):
#            if (i, j) in lookup:
#                s += 'X'
#            else:
#                s += '-'
#            s += ' '
#        s += '\n'
#    
#    print(s)
            
#            
#deposits = [(0, 4,.3), (6, 2, 3), (3, 7, 2.2), (5, 5, .5), (3, 5, .8), (7, 7, .3)]
#display(deposits, 0, 8, 0, 8)

def tons_inside(deposits, top, bottom, left, right):
    """Returns the total number of tons of deposits for which the row is at least top,
    but strictly less than bottom, and the column is at least left, but strictly
    less than right."""
    # Do not alter the function header.  
    # Just fill in the code so it returns the correct number of tons.
    lookup = {}
    s = ''
    for t in deposits:
        lookup[(t[0], t[1])] = t[2]
        
    for i in range(top, bottom):
        for j in range(left, right):
            if (i, j) in lookup:
                s += str(lookup[(i, j)])
            else:
                s += '-'
            s += ' '
        s += '\n'
    
    print(s) 
    
deposits = [(0, 4,.3), (6, 2, 3), (3, 7, 2.2), (5, 5, .5), (3, 5, .8), (7, 7, .3)]
tons_inside(deposits, 0, 8, 0, 8)