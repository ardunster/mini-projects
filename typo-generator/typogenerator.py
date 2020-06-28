#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 12:04:12 2020

@author: adunster
"""

'''
typos to include:
    skip random letter in mid word (especially between o and e)
    o = oe
    th = ht
    p = o
    the = hte
    ask = aks
    and = adn
    ie = ei
    l = I 
    I = l
    
'''

if __name__ == '__main__':
    print('**~~~~Welcome to Typo Generator 25000!!!~~~~**\n')
    print('The Latest and Greatest script to randomly introduce errors into perfectly good text.',
          '\nGuaranteed to drive your neighborhood grammar nazis crazy!\n')
    print('What\'s your name?')
    user_name = input('> ')
    
    print(f'\nGreat, {user_name}! What text would you like to generate errors in?')
    
    # while playing:
    # get input
    # verify input is usable
    # apply a random error
    # check for valid errors first, or try to apply one at random, try a different one if it doesn't work?
    # after generating errored result, ask: "Reroll, New Sentence, Exit"
    
    print(f'Thanks for using Typo Generator 25,000, {user_name}! Run the script again to play again. Have a nice day!')