# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 16:34:53 2020

@author: ardunster
"""

#Dice roller script. For D&D and any other game requiring randomized rolls.
#Dice size are not limited to traditional dice. You can roll any die you want.

import random
import datetime

print('Input desired dice roll in xdy format, ie, 1d6.')

dice_input = input('Roll: ')


#Validate format
while (not 'd' in dice_input) or (int(dice_input.count('d')) > 1):
    print('Please enter desired dice roll in xdy format.')
    dice_input = input('Roll: ')

d = int(dice_input.index('d'))

dice_qty = int(dice_input[:d])

dice_size = int(dice_input[d+1:])


# Roll Dice

roll = []

for i in range(dice_qty):
    roll.append(random.randrange(1, dice_size))


#Return results
if dice_qty > 1:
    print(f'You rolled {dice_qty}d{dice_size}, resulting in rolls of:')
else:
    print(f'You rolled {dice_qty}d{dice_size}, resulting in a roll of:')
print(roll)
print(f'Your total roll is {sum(roll)}.')


#Log results with timestamp

now = datetime.datetime.now()

roll_log = open('roll_log.txt', 'a')

roll_log.write(f'{now}\nRolled {dice_qty}d{dice_size}, resulting in {roll}, total {sum(roll)}.\n')

roll_log.close()
