#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 16:49:38 2020

@author: adunster
"""

'''
    * Prime Factorization - Have the user enter a number and find all Prime 
    Factors (if there are any) and display them.

Not a 1 week project but wanted to try this short one, too.
'''


'''
Steps:
    - get user input
    - verify integer greater than 1
    - find primes:
        if x / y == 0, then factor.
        if y is not prime, subdivide.
        with list of factors, pick out primes.
        use  the other program to find primes? or math module.

'''

from  cpb_final import is_prime


def get_int(question_string):
    '''
    Retrieves and verifies input is integer.
    Input: A string to use as the input request.
    Output: integer of user's input.
    '''
    user_input = ''
    while user_input == '':
        user_input = input(question_string)
        if user_input.isdigit():
            return int(user_input)
        else:
            print('Invalid input. Please enter an integer.')
            user_input = ''



def factorize(number):
    '''
    Returns the prime factors of input.
    '''
    poss_factors = []
    ver_factors = []
    
    for i in range(1,number):
        if is_prime(i+1) and number % (i+1) == 0:
            poss_factors.append(i+1)
    
    while number > 1:
        for i in poss_factors:
            if number % i == 0:
                number = number / i
                ver_factors.append(i)
        
    return ver_factors


if __name__ == '__main__':
    user_number = get_int('Enter a number to factorize: ')
    print(factorize(user_number))
