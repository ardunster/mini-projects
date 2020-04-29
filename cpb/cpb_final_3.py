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

import geopy

def locate_city():
    '''
    Fetch from web city's Lat/Long location.
    '''
    pass


def get_city():
    '''
    Gets city name and country from user.
    '''
    pass


def calc_distance(pointa,pointb):
    '''
    Use Lat/Long information to calculate distance between two points.
    '''
    pass

def unit_input():
    '''
    Gets user input to select unit of measurement to display distance in.
    '''
    pass


if __name__ == '__main__':
    print('run code here')
    #while city1:
    # input city 1 
    #fetch city info
    # verify lat, lon, location, option to re-enter city 1 if incorrect.
    # ditto city 2
    #inout to select unit of distance
    # displays calculated distance

'''
Next steps:
figure out how to fetch geodata
see what format data needs passed to fetch
code get_city() to output correct data, and/or call locate_city() in itself and 
output location
calculate distance in most convenient measurement
program input for unit of measure
convert unit of measure
display conversion with all relevant data. IE, City A is at x,y. City B is at x2,y2. 
Distance is z units from A to B. 

After this:
UI for roller.
'''