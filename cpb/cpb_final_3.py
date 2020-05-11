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
from geopy import distance

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


def verify_city(location_input):
    if isinstance(location_input, geopy.location.Location):
        return True
    else:
        return False


def get_city():
    '''
    Gets city name and country from user.
    Output: Geocode location.Location object.
    '''
    
    user_input = ''
    
    while user_input == '':
        user_input = input('Enter a city or other location: ')
        user_location = locate_city(user_input)
        if verify_city(user_location):
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
        user_input = input('Select from the following options:\n1: Miles   2: Kilometers   3: Feet \
                           \n4: Meters  5: Leagues      6: Nautical Miles\n: ')
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
            verify = input('You have selected meters, is this correct? ')
            if verify_yn(verify):
                return 'meters'
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
        


def calc_distance(pointa,pointb):
    '''
    Use Lat/Long information to calculate distance between two points.
    '''
    
    a = (pointa.latitude, pointa.longitude)
    b = (pointb.latitude, pointb.longitude)
    
    dist = distance.distance(a,b).miles
    
    return dist

def convert_distance(distance,new_uom='miles'):
    '''
    Takes a distance in x unit and converts to input unit.
    Valid UOM inputs: 'miles', 'kilometers', 'feet', 'meters', 'leagues', 'nau_miles'
    Output: float
    '''
    
    if new_uom == 'miles':
        dist_converted = "{:.2f}".format(distance) + ' miles'
    elif new_uom == 'kilometers':
        dist_converted = "{:.2f}".format(distance * 1.609344) + ' kilometers'
    elif new_uom == 'feet':
        dist_converted = "{:.2f}".format(distance * 5280) + ' feet'
    elif new_uom == 'meters':
        dist_converted = "{:.2f}".format(distance * 1609.344) + ' meters'
    elif new_uom == 'leagues':
        dist_converted = "{:.2f}".format(distance / 3) + ' leagues'
    elif new_uom == 'nau_miles':
        dist_converted = "{:.2f}".format(distance * 0.86897624190065) + ' nautical miles'
    else:
        raise ValueError('Invalid unit of measurement: {}'.format(new_uom))
        
    return dist_converted


if __name__ == '__main__':
    print('Welcome to magical distance calculator, where you can enter two locations \
          and a unit of measure and MAGICALLY receive the distance between them in return!')
    print('For your first location:')
    pointa = get_city()
    print('And for your second location:')
    pointb = get_city()
    dist = calc_distance(pointa,pointb)
    print('Now, how would you like to measure your MAGICAL result?')
    unit_of_measure = unit_input()
    dist_converted = convert_distance(dist,unit_of_measure)
    
    print('As if by magic, the following appears before your eyes:\n{a} (the first location you selected) is {d} away from {b} (the second location you selected).\nIsn\'t that amazing????\n'.format(a=pointa.address, b=pointb.address, d=dist_converted))
    print('And were you wondering? I know you were...\n{a} is at {alat},{alon}, and {b} is at {blat},{blon}. Now you know! :D'.format(a=pointa.address,alat=pointa.latitude,alon=pointa.longitude,b=pointb.address,blat=pointb.latitude,blon=pointb.longitude))



'''
Next steps:



This is going super fast and is not a week long project, 2 hours in and I have 
everything but the calculations.

New idea: let's figure out how to slap an UI on it! :D

After this:
UI for roller.
'''