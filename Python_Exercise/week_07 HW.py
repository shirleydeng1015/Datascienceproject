#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 17:14:04 2018

@author: shirleydeng
"""
import random 

class playing_card:        
        
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit   
    
    def __repr__(self):
        return "%s of %s" % (self.rank, self.suit)
            
        
class deck:
    ALL_RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    ALL_SUITS = ["♠", "♥", "♦", "♣"]
    
    def __init__(self, defined_suit = ALL_SUITS):
        self.cards = self.init_cards(defined_suit)
        
    def init_cards(self, suits):
        cards = []
        for suit in suits:
            for rank in self.ALL_RANKS:
                card = playing_card(rank, suit)
                cards.append(card)
        return cards
        
    def shuffle_deck(self):
        random.shuffle(self.cards)
    
    def deal_card(self, card_count):
        ret = self.cards[:card_count]
        self.cards = self.cards[card_count:]
        return ret
        
    
        
all_suits_deck = deck() #an instance of deck Class
all_suits_deck.shuffle_deck()
print(all_suits_deck.deal_card(52))

one_suit_deck = deck("♥")
one_suit_deck.shuffle_deck()
print(one_suit_deck.deal_card(10))
    
    
    

