#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 12:04:12 2020

@author: adunster
"""

import random

'''
typos to include:
    skip random letter in mid word (especially consonant between vowel and e)
    random swap of letters
    random removal of whitespace or punctuation
    random insertion of whitespace or punctuation (punctuation near proximate letters)
    displacement of punctuation back one space
    turn capital letter lower case, move capitalization to different letter
    take character requiring shift key and convert to same keyboard location without shift
    insertion of proximate letter
    extra e after t or d at end of word
    o = oe
    th = ht
    p = o
    the = hte
    ask = aks
    and = adn
    ie = ei
    l = I 
    I = l
    x = z
    n = b
    o = i
    m = n
    take entire word and shift letters used by one hand right or left by one keyboard space
    
'''

class TypoError(Exception):
    pass


def get_input():
    '''
    Asks for user input, verifies that it's at least something like a 
    sentence (longer than 3 characters, not all digits, contains vowels), and 
    returns string
    '''
    output = ''
    while output == '':
        output = input('Please enter a sentence:\n> ')
        if len(output) <= 3:
            print('That\'s pretty short, don\'t you think? Try something longer.')
            output = ''
        elif output.isdigit() == True:
            print('Thought you could fool me with a number? Try again!')
            output = ''
        elif not (set(output) & set(('a', 'e', 'i', 'o', 'u'))):
            print('I\'m pretty sure it\'s not actually a sentence with no vowels. Try again!')
            output = ''
            
    return output

def random_typo(user_input):
    '''
    Takes a string as an argument, selects a random typo function to apply, returns
    a string of a successful result.
    '''
    
    typos = [typo_1, typo_2, typo_3]
    while True:
        try:
            return random.choice(typos)(user_input)
        except TypoError as e:
            print(f'e = {e}')
            continue
    
    

def typo_1(string):
    print(f'Typo 1 of {string}')
    
def typo_2(string):
    print(f'Typo 2 of {string}')

def typo_3(string):
    print(f'Typo 3 of {string}')
    raise TypoError


if __name__ == '__main__':
    # print('**~~~~Welcome to Typo Generator 25,000!!!~~~~**\n')
    # print('The Latest and Greatest script to randomly introduce errors into perfectly good text.',
    #       '\nGuaranteed to drive your neighborhood grammar nazis crazy!\n')
    # print('First, introductions! What\'s your name?')
    # user_name = input('> ')
    
    # print(f'\nGreat, {user_name}! What text would you like to generate errors in?')
    
    # user_input = get_input()
    
    test_string = 'Test string'
    
    random_typo(test_string)
    
    # while playing:
    # get input
    # verify input is usable
    # apply a random error
    # check for valid errors first, or try to apply one at random, try a different one if it doesn't work?
    # How many errors to generate? add 1 per x words/characters, or, random of range of x per y characters. 
    # after generating errored result, ask: "Reroll, New Sentence, Exit"
    
    # print(f'Thanks for using Typo Generator 25,000, {user_name}! Run the script again to play again. Have a nice day!')

