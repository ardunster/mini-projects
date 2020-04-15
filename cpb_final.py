#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 10:12:22 2020

@author: adunster
"""

'''
Final Project for Udemy Course Complete Python Bootcamp.
Objectives:
    From a list of potential projects (https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/12-Final%20Capstone%20Python%20Project/02-Final%20Capstone%20Project%20Ideas.ipynb),
    select 1 one-day project, and 1 one-week project, to create code for.
Personal objectives:
    Also create testing for projects, comment code as appropriate, keep it clean

Project Candidates:
    * Prime Factorization - Have the user enter a number and find all Prime 
    Factors (if there are any) and display them.
    * Next Prime Number - Have the program find prime numbers until the user 
    chooses to stop asking for the next one.
    * Distance Between Two Cities - Calculates the distance between two cities
    and allows the user to specify a unit of distance. This program may require
    finding coordinates for the cities like latitude and longitude.
    - Happy Numbers - A happy number is defined by the following process. 
    Starting with any positive integer, replace the number by the sum of the 
    squares of its digits, and repeat the process until the number equals 1 
    (where it will stay), or it loops endlessly in a cycle which does not 
    include 1. Those numbers for which this process ends in 1 are happy numbers,
    while those that do not end in 1 are unhappy numbers. Display an example of
    your output here. Find first 8 happy numbers.
    - Number Names - Show how to spell out a number in English. You can use a 
    preexisting implementation or roll your own, but you should support inputs 
    up to at least one million (or the maximum value of your language's default
    bounded integer type, if that's less). Optional: Support for inputs other 
    than positive integers (like zero, negative integers, and floating-point 
    numbers).
    * Collatz Conjecture - Start with a number n > 1. Find the number of steps 
    it takes to reach one using the following process: If n is even, divide it
    by 2. If n is odd, multiply it by 3 and add 1.
    - Product Inventory Project - Create an application which manages an 
    inventory of products. Create a product class which has a price, id, and 
    quantity on hand. Then create an inventory class which keeps track of 
    various products and can sum up the inventory value.
    - Online White Board - Create an application which allows you to draw 
    pictures, write notes and use various colors to flesh out ideas for 
    projects. Optional: Add feature to invite friends to collaborate on a white 
    board online.
    - Quiz Maker - Make an application which takes various questions from a 
    file, picked randomly, and puts together a quiz for students. Each quiz can 
    be different and then reads a key to grade the quizzes.
    * Budget Tracker - Write an application that keeps track of a household’s b
    udget. The user can add expenses, income, and recurring costs to find out 
    how much they are saving or losing over a period of time. Optional: Allow 
    the user to specify a date range and see the net flow of money in and out 
    of the house budget for that time period.
    - Turtle Graphics - This is a common project where you create a floor of 
    20 x 20 squares. Using various commands you tell a turtle to draw a line on 
    the floor. You have move forward, left or right, lift or drop pen etc. Do a 
    search online for "Turtle Graphics" for more information. Optional: Allow 
    the program to read in the list of commands from a file.
    
    
'''

'''
1 day project: generator that produces the next prime number.
'''

import math

def is_prime(n):
    '''Checks if number is prime or not.'''
    if n >= 1:
        if n == 1:
            return True
        elif n == 2:
            return True
        elif n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n) + 1), 2):
            if n % i == 0:
                return False
        return True
    return False

def next_prime(num=1):
    '''
    Generator that looks for next prime number
    Call with an integer to choose starting position, defaults to 1
    '''
    while True:
        while not is_prime(num):
            num += 1
        yield num
        num += 1

def ask_next(x=1):
    '''
    Input frame for running next_prime()
    Call with an integer to choose starting position, defaults to 1
    '''
    next_p = next_prime(x)
    again = ''
    print('Your first prime is: {}'.format(next(next_p)))
    while again == '':
        again = input('Next? y/n\n')
        if again == '' or again[0].lower() == 'y':
            again = ''
        elif again[0].lower() == 'n':
            print('Thanks for using PrimeFinder!!! Please come again.')
            break
        else:
            print('Invalid input.\n')
            again = ''
        print('Your next prime is: {}'.format(next(next_p)))


if __name__ == "__main__":
    ask_next()