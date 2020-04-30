#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 18:52:03 2020

@author: adunster
"""

'''

Second half of Complete Python Bootcamp Final Project:
Select a project that will take a week to finish.
(For more information see cpb_final.py)

My candidates:
    * Distance Between Two Cities - Calculates the distance between two cities
    and allows the user to specify a unit of distance. This program may require
    finding coordinates for the cities like latitude and longitude.
    - Online White Board - Create an application which allows you to draw 
    pictures, write notes and use various colors to flesh out ideas for 
    projects. Optional: Add feature to invite friends to collaborate on a white 
    board online.
    - Quiz Maker - Make an application which takes various questions from a 
    file, picked randomly, and puts together a quiz for students. Each quiz can 
    be different and then reads a key to grade the quizzes.
    - Turtle Graphics - This is a common project where you create a floor of 
    20 x 20 squares. Using various commands you tell a turtle to draw a line on 
    the floor. You have move forward, left or right, lift or drop pen etc. Do a 
    search online for "Turtle Graphics" for more information. Optional: Allow 
    the program to read in the list of commands from a file.
    
'''


'''
1-week project: 
    Distance Between Two Cities - Calculates the distance between two cities
    and allows the user to specify a unit of distance. This program may require
    finding coordinates for the cities like latitude and longitude.
'''

# Imports

import geopy
import time

# Functions 

def locate_city(location_input):
    '''
    Fetch geocode for given location.
    Input: String of location to fetch.
    Output: Geocode location.Location object.
    '''
    
    geolocator = geopy.geocoders.Nominatim(user_agent="CPB Final Project", timeout=5)
    
    location = geolocator.geocode(location_input)
    
    return location


def get_city():
    '''
    Gets city name and country from user.
    Output: Geocode location.Location object.
    '''
    
    user_input = ''
    
    while user_input == '':
        user_input = input('Enter a city or other location: ')
        user_location = locate_city(user_input)
        if isinstance(user_location, geopy.location.Location):
            print('\nFound: {}'.format(user_location))
            verify = input('Is this correct? y/n: ')
            if verify[0].lower() == 'y':
                print('\nSaved!\n')
                return user_location
            else:
                print('\nPlease retry.')
                user_input = ''
        else:
            print('\nInvalid input.')
            time.sleep(1) # to reduce timeouts from trying too many times in a row.
            user_input = ''
        

def unit_input():
    '''
    Gets user input to select unit of measurement to display distance in.
    Output: string of selected unit.
    '''
    
    user_input = ''

    def verify_yn(string):
        '''Checks if input string counts as yes or no.'''
        if string[0].lower() == 'y':
            return True
        else:
            return False
    
    while user_input == '':
        user_input = input('Select from the following options:\n1: Miles        2: Kilometers   3: Feet \
                           \n4: Centimeters  5: Leagues      6: Nautical Miles\n: ')
        if not user_input[0].isdigit():
            print('Invalid input, please select by number.')
            user_input = ''
        elif int(user_input[0]) == 1:
            verify = input('You have selected miles, is this correct? ')
            if verify_yn(verify):
                return 'miles'
            else:
                print('\nPlease try again.')
                user_input = ''
        elif int(user_input[0]) == 2:
            verify = input('You have selected kilometers, is this correct? ')
            if verify_yn(verify):
                return 'kilometers'
            else:
                print('\nPlease try again.')
                user_input = ''
        elif int(user_input[0]) == 3:
            verify = input('You have selected feet, is this correct? ')
            if verify_yn(verify):
                return 'feet'
            else:
                print('\nPlease try again.')
                user_input = ''
        elif int(user_input[0]) == 4:
            verify = input('You have selected centimeters, is this correct? ')
            if verify_yn(verify):
                return 'centimeters'
            else:
                print('\nPlease try again.')
                user_input = ''
        elif int(user_input[0]) == 5:
            verify = input('You have selected leagues, is this correct? ')
            if verify_yn(verify):
                return 'leagues'
            else:
                print('\nPlease try again.')
                user_input = ''
        elif int(user_input[0]) == 6:
            verify = input('You have selected nautical miles, is this correct? ')
            if verify_yn(verify):
                return 'nau_miles'
            else:
                print('\nPlease try again.')
                user_input = ''
        else:
            print('Invalid input, please try again.')
            user_input = ''
        


def calc_distance(pointa,pointb,uom='miles'):
    '''
    Use Lat/Long information to calculate distance between two points.
    '''
    pass




if __name__ == '__main__':
    pass
#    print('Welcome to magical distance calculator, where you can enter two locations \
#          and a unit of measure and MAGICALLY receive the distance between them in return!')
#    print('For your first location:')
#    pointa = get_city()
#    print('And for your second location:')
#    pointb = get_city()
#    print('Now, how would you like to measure your MAGICAL result?')
#    unit_of_measure = unit_input()
    #input to select unit of distance
    # displays calculated distance

'''
Next steps:

calculate distance in most convenient measurement
program input for unit of measure
convert unit of measure
display conversion with all relevant data. IE, City A is at x,y. City B is at x2,y2. 
Distance is z units from A to B. 

This is going super fast and is not a week long project, 2 hours in and I have 
everything but the calculation.

New idea: let's figure out how to slap an UI on it! :D

After this:
UI for roller.
'''