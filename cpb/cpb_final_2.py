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



def get_input(question_string,type_to_verify):
    pass

def factorize(number):
    pass


if __name__ == '__main__':
    print('run code here')
    user_number = get_input('Enter a number to factorize: ',int)
    factorize(user_number)
