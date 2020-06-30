#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 12:04:12 2020

@author: adunster
"""

import random
import re


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
        elif not (set(output.lower()) & set(('a', 'e', 'i', 'o', 'u'))):
            print('I\'m pretty sure it\'s not actually a sentence with no vowels. Try again!')
            output = ''
        elif len(output) >= 300:
            print('Distribution of typos gets improbable in longer texts. Try something smaller! (Feel free to petition for longer inputs in TypoGen 2.0 :D)')
            output = ''
            
    return output


def random_typo(user_input,typos):
    '''
    Takes a string as an argument, selects a random typo function to apply, returns
    tuple of a string of a successful result and the index of function used. 
    Retries random typos until one works.
    '''
    
    while True:
        try:
            choice = random.randrange(len(typos))
            return typos[choice](user_input), choice
        except TypoError:
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
    
        if choice == '':
            print('Please make a selection.\n')
        elif choice[0].lower() == 'r':
            output = 'r'
            print('Rerolling errors!')
        elif choice[0].lower() == 'n':
            output = 'n'
            print('New entry!')
        elif choice[0].lower() == 'e' or choice[0].lower() == 'x':
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
    elif re_match.group() == "'" or re_match.group() == '"' and re_match.start() == 0:
        # Fix issue where moving a quote mark at the beginning of the string could cause unintended results
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
    

def typo_8(string):
    '''Typo introduction: random capitalization of leading letter in a word'''
    working = string.split()
    if len(working) == 1:
        raise TypoError
    elif string.isupper():
        raise TypoError
    else:
        rand_num = random.randrange(1,len(working))
        working[rand_num] = working[rand_num].capitalize()
        output = ' '.join(working)
    
    return output


def typo_9(string):
    '''Typo introduction: replace a character that requires the shift key with the same keyboard position without it'''
    re_match = re.search('[!@#$%^&*()_+:<>?]{1}', string)
    if not re_match:
        raise TypoError    
    else:
        char_dict = {'!':'1', '@':'2', '#':'3', '$':'4', '%':'5', '^':'6', '&':'7',
                     '*':'8', '(':'9', ')':'0', '_':'-', '+':'=', ':':';', '<':',',
                     '>':'.', '?':'/'}
        char = char_dict[re_match.group()]

        output = string[:re_match.start()] + char + string[re_match.end():]
        
    return output


def typo_10(string):
    '''Typo introduction: picks a random word from input, shifts letters of one hand by 1 keyboard position toward center'''
    working = string.split()
    working2 = []
    
    shift_lh = {'q':'w', 'w':'e', 'e':'r', 'r':'t', 't':'y', 'a':'s', 's':'d', 
                'd':'f', 'f':'g', 'g':'h', 'z':'x', 'x':'c', 'c':'v', 'v':'b',
                'Q':'W', 'W':'E', 'E':'R', 'R':'T', 'T':'Y', 'A':'S', 'S':'D',
                'D':'F', 'F':'G', 'G':'H', 'Z':'X', 'X':'C', 'C':'V', 'V':'B'}
    shift_rh = {'p':'o', 'o':'i', 'i':'u', 'u':'y', 'y':'t', ';':'l', 'l':'k',
                'k':'j', 'j':'h', '.':',', ',':'m', 'm':'n', 'n':'b', 'P':'O', 
                'O':'I', 'I':'U', 'U':'Y', 'Y':'T', ':':'L', 'L':'K', 'K':'J', 
                'J':'H', '>':'<', '<':'M', 'M':'N', 'N':'B', '?':'>'}
    
    if len(working) == 1:
        raise TypoError
    else:
        rand_num = random.randrange(1,len(working))
        re_lh = re.search('[qwertasdfgzxcv]', working[rand_num])
        re_rh = re.search('[yuiophjkl;.,mn]', working[rand_num])
        if re_lh and re_rh:
            choice = random.choice((shift_rh,shift_lh))
        elif re_lh:
            choice = shift_lh
        elif re_rh:
            choice = shift_rh
        else:
            raise TypoError
        output = ''
        for char in working[rand_num]:
            if char in choice.keys():
                output += choice[char]
            else: 
                output += char
        
    for i in range(len(working)):
        if i == rand_num:
            working2.append(output)
        else:
            working2.append(working[i])
    
    output = ' '.join(working2)
    
    return output


def typo_11(string):
    '''Typo introduction: random doubling of character other than space'''
    output = ''
    rand_num = random.randrange(1,len(string))
    
    for i in range(len(string)):
        if i == rand_num:
            if string[i] == ' ':
                rand_num += 1
            else:
                output += (string[i] * 2)
        else:
            output += string[i]
            
    return output


def typo_12(string):
    '''Typo introduction: adds e after t or d at end of word'''
    re_match = re.search('[td]\\b',string)
    if not re_match:
        raise TypoError
    else:
        output = string[:re_match.start()+1] + 'e' + string[re_match.end():]
        
    return output


def typo_13(string):
    '''Typo introduction: random character swap into common errors'''
    re_match = re.search('[oplIxnmt,.]', string)
    if not re_match:
        raise TypoError
    
    errors = {'o':('oe','p', 'i', '9', '0'), 'p':('o', '[', '-', '0', ';'), 
              'l':'I', 'I':'l', 'x':'z', 'n':'b', 'm':'n', 't':'g', ',':('m', 'k', 'l'),
              '.':('l', ';')}
    output = ''
    
    while output == '':
        rand_num = random.randrange(len(string))
        if string[rand_num] in errors.keys():
            for i in range(len(string)):
                if i == rand_num:
                    output += random.choice(errors[string[i]])
                else:
                    output += string[i]
   
    return output


def typo_14(string):
    '''Typo introduction: adds g or d after n at end of word'''
    re_match = re.search('[n]\\b',string)
    if not re_match:
        raise TypoError
    else:
        output = string[:re_match.start()+1] + random.choice(('g', 'd')) + string[re_match.end():]
        
    return output

def typo_15(string):
    '''Typo introduction: removes h from th, sh, wh, or ch'''
    re_match = re.search('[tswc]h{1}',string)
    if not re_match:
        raise TypoError
    else:
        output = string[:re_match.start()+1] + string[re_match.end():]
        
    return output


def typo_16(string):
    '''Typo introduction: destruction of you're'''
    re_match = re.search("you're", string)
    if not re_match:
        raise TypoError
    else:
        output = string[:re_match.start()] + random.choice(('your', 'yor', 'youre', 'yer')) + string[re_match.end():]
        
    return output


def typo_17(string):
    '''Typo introduction: destruction of they're'''
    re_match = re.search("they're", string)
    if not re_match:
        raise TypoError
    else:
        output = string[:re_match.start()] + random.choice(('their', 'thier', 'theyre', 'there', 'three', 'ther', 'theyr')) + string[re_match.end():]
        
    return output


def typo_18(string):
    '''Typo introduction: accidental capslock'''
    if not string[0].isupper():
        raise TypoError
    else: 
        output = string.upper()
    
    return output


def typo_19(string):
    '''Typo introduction: replace nd with dn, th with ht, etc'''
    re_match = re.search('th|nd|ng|ch|sh', string)
    errors = {'th':'ht','nd':'dn','ng':'gn','ch':'hc','sh':'hs'}
    if not re_match:
        raise TypoError
    else:
        output = string[:re_match.start()] + errors[re_match.group()] + string[re_match.end():]
        
    return output






# list of all possible typo introduction functions, used for random choice of typo
typos = [typo_1, typo_2, typo_3, typo_4, typo_5, typo_6, typo_7, typo_8, typo_9,
         typo_10, typo_11, typo_12, typo_13, typo_14, typo_15, typo_16, typo_17,
         typo_18, typo_19]

# characters per typo introduction. Higher number = lower chance of typos.
typo_frequency = 15




if __name__ == '__main__':
    print('**~~~~Welcome to Typo Generator 25,000!!!~~~~**\n')
    print('The Latest and Greatest script to randomly introduce errors into perfectly good text.',
            '\nGuaranteed to drive your neighborhood grammar nazis crazy!\n')
    print('First, introductions! What\'s your name?')
    user_name = input('> ')
    
    print(f'\nGreat, {random_typo(user_name, typos)[0]}! What text would you like to generate errors in?')
    
    running = True
    while  running == True:
        # New sentence loop
        user_input = get_input()
        
        while True:
            # Reroll loop
            loop_typos = list(typos)
            output_string = user_input
            
            if (len(output_string)//typo_frequency) > 1:
                errors_to_gen = random.randrange(1,(len(output_string)//typo_frequency))
            else:
                errors_to_gen = 1
    
            for i in range(errors_to_gen):
                new_typo = random_typo(output_string, loop_typos)
                output_string = new_typo[0]
                loop_typos.pop(new_typo[1])
                if len(loop_typos) < errors_to_gen - i:
                    for i in range(len(typos)):
                        loop_typos.append(typos[i])
                
            print(f'\nResult: {output_string}')

            
            reroll = reroll_or()
            
            if reroll == 'e':
                running = False
                break
            elif reroll == 'n':
                break
            elif reroll == 'r':
                continue
    
    print(f'Thanks for using Typo Generator 25,000, {random_typo(user_name, typos)[0]}! Run the script again to play again. Have a nice day!')

