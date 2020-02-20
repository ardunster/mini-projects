# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 15:59:33 2020

@author: ardunster
"""

print('Enter numbers separated to receive mean and median. Enter \'done\'\
 to stop entry and calculate your answer.')

mean_list = []

mean_input = ''

while (not mean_input.lower() == 'done'):
    mean_input = input('Enter a number.\n> ')
    if mean_input.lower() == 'done':
        print('Okay, your final list, in order, is:')
    elif (not mean_input.isdigit()) and (not mean_input.lower() == 'done'):
        print('Please enter numbers only.')
    else: 
        mean_list.append(int(mean_input))

#Show them their entries.
mean_list = sorted(mean_list)
print(mean_list)

#Find the median.
length = len(mean_list)
q = int(length / 2)

if length % 2:
    median = mean_list[q]
else:
    median = (mean_list[q-1] + mean_list[q]) / 2

#Show results.
print(f'The sum of your entries, {sum(mean_list)}, divided by the number of \
entries in your list, {len(mean_list)}, results in a mean of \
{sum(mean_list) / len(mean_list)}, and has a median of {median}.')
