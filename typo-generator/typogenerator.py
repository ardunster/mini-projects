#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 12:04:12 2020

@author: adunster
"""

import random
import re

'''
typos to include:
    # skip random letter in mid word (especially consonant between vowel and e)
    # random swap of letters
    # random removal of whitespace or punctuation
    # random insertion of whitespace or punctuation (punctuation near proximate letters)
    # displacement of punctuation back one space
    # turn capital letter lower case, move capitalization to different letter
    random capitalization of leading letter of word
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
    m = n
    o = p
    p = [, -, 0, ;
    o = i, p, 9 or 0
    t = g
    take entire word and shift letters used by one hand right or left by one keyboard space
    double a random letter
    sentence starting in caps converted to all caps
    you're = your or youre
    they're = their or there or theyre
    remove h from th, sh, etc
    replace punctuation with proximate letter
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

def random_typo(user_input,typos):
    '''
    Takes a string as an argument, selects a random typo function to apply, returns
    a string of a successful result. Retries random typos until one works.
    '''
    
    while True:
        try:
            return random.choice(typos)(user_input)
        except TypoError:
            print('error')
            continue

def reroll_or():
    '''
    Validates input if player would like to reroll, play with a new string, or exit.
    Output: a single letter representing one of the three options.
    '''
    choice = ''
    
    while choice == '':
        print('Would you like to [R]eroll the errors on the current sentence, enter a [N]ew sentence, or [E]xit?')
        choice = input('> ')
    
        if choice[0].lower() == 'r':
            output = 'r'
            print('Rerolling errors!')
        elif choice[0].lower() == 'n':
            output = 'n'
            print('New entry!')
        elif choice[0].lower() == 'e':
            output = 'e'
            print('Exiting....')
        else:
            print('Invalid choice, try again.\n')
            choice = ''
        
    return output
        
    

def typo_1(string):
    '''Typo introduction: skip a random character. Tries consonant between a vowel and e first.'''
    vce_pattern = re.compile('[aeiou][^aeiou]e') #should match vowel, consonant, e
    re_match = vce_pattern.search(string)
    if re_match:
        output = string[:re_match.start()+1] + string[re_match.end()-1:]
    else:
        rand_num = random.randrange(1,(len(string)-1))
        output = string[:rand_num-1] + string[rand_num:]
    return output


def typo_2(string):
    '''Typo introduction: random swap of two adjacent characters in input'''
    rand_num = random.randrange(1,(len(string)-1))
    output = string[:rand_num-1] + string[rand_num] + string[rand_num-1] + string[rand_num+1:]
    return output


def typo_3(string):
    '''Typo introduction: random removal of whitespace or punctuation'''
    re_match = re.search('[ .,?!]', string)
    if not re_match:
        raise TypoError
    else:
        chars = [pos for pos,char in enumerate(string) if char in (' ',',','.','?','!')]
        rand_num = random.choice(chars)
        output = string[:rand_num] + string[rand_num+1:]
    
    return output


def typo_4(string):
    '''Typo introduction: random addition of whitespace'''
    rand_num = random.randrange(1,(len(string)-1))
    output = string[:rand_num] + ' ' + string[rand_num:]
    return output


def typo_5(string):
    '''Typo introduction: addition of punctuation in reasonably possible location'''
    re_match = re.search('[mklp]', string)
    if not re_match:
        raise TypoError
    else:
        rand_num = random.choice((0,1))
        if re_match.group() == 'm' or re_match.group() == 'k':
            output = string[:re_match.start()+rand_num] + ',' + string[re_match.start()+rand_num:]
        elif re_match.group() == 'l':
            r_punct = random.choice((',','.',';'))
            output = string[:re_match.start()+rand_num] + r_punct + string[re_match.start()+rand_num:]
        elif re_match.group() == 'p':
            r_punct = random.choice((';','[','-',''))
            output = string[:re_match.start()+rand_num] + r_punct + string[re_match.start()+rand_num:]

    return output


def typo_6(string):
    '''Typo introduction: displacement of punctuation'''
    re_match = re.search('[\'",.;?!]', string)
    if not re_match:
        raise TypoError
    else:
        output = string[:re_match.start()-1] + string[re_match.start()] + string[re_match.start()-1] + string[re_match.end():]
        
    return output
    
def typo_7(string):
    '''Typo introduction: displacement of capitalization'''
    re_match = re.search('[A-Z]{1}', string)
    if not re_match:
        raise TypoError
    elif string[re_match.start() + 1].isupper():
        raise TypoError
    else:
        output = string[:re_match.start()+1].lower() + string[re_match.start()+1].upper() + string[re_match.start()+2:]
    
    return output
    
    
    
    
        # output = string[:re_match.start()+rand_num] + ' ' + string[re_match.start()+rand_num:]
        
        

# list of all possible typo introduction functions
typos = [typo_1, typo_2, typo_3, typo_4, typo_5, typo_6, typo_7]

# characters per typo introduction
typo_frequency = 15


if __name__ == '__main__':
    # print('**~~~~Welcome to Typo Generator 25,000!!!~~~~**\n')
    # print('The Latest and Greatest script to randomly introduce errors into perfectly good text.',
    #       '\nGuaranteed to drive your neighborhood grammar nazis crazy!\n')
    # print('First, introductions! What\'s your name?')
    # user_name = input('> ')
    
    # print(f'\nGreat, {user_name}! What text would you like to generate errors in?')
    
    # while running:
        # get the input
        # apply the typos
        # ask if we want to reroll the current typos, enter a new sentence, or exit.
    # user_input = get_input()
    
    test_string = 'Test string longer! With some extra stuff, gotta make this long enough to work, right? How many errors can we GET anyway?'
    
    # print(random_typo(test_string, typos))
    
    # while playing:
    # get input
    # verify input is usable
    # apply a random error
    # check for valid errors first, or try to apply one at random, try a different one if it doesn't work?
    # How many errors to generate? add 1 per x words/characters, or, random of range of x per y characters. 
    
    # output_string = user_input
    output_string = test_string
    
    if (len(output_string)//typo_frequency) > 1:
        errors_to_gen = random.randrange(1,(len(output_string)//typo_frequency))
    else:
        errors_to_gen = 1
    
    for _ in range(errors_to_gen):
        output_string = random_typo(output_string, typos)
        
    print(f'Result: {output_string}, {errors_to_gen}')
    
    # after generating errored result, ask: "Reroll, New Sentence, Exit"
    
    # print(f'Thanks for using Typo Generator 25,000, {user_name}! Run the script again to play again. Have a nice day!')

# There is unfortunately a chance of repeating the same error multiple times in 
# a result that does not make sense (moving initial capital 3 letters over, for example).
# This maybe could be fixed by making a fresh copy of the typos list for each 
# string processed and .pop() the typo used. 
# will try if I have time, low priority

