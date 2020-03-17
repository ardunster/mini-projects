#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 16:25:58 2020

@author: adunster
"""

'''
Challenge #383 from: https://www.reddit.com/r/dailyprogrammer/comments/ffxabb/20200309_challenge_383_easy_necklace_matching/

Imagine a necklace with lettered beads that can slide along the string. Here's
an example image. In this example, you could take the N off NICOLE and slide 
it around to the other end to make ICOLEN. Do it again to get COLENI, and so 
on. For the purpose of today's challenge, we'll say that the strings "nicole", 
"icolen", and "coleni" describe the same necklace.

Generally, two strings describe the same necklace if you can remove some 
number of letters from the beginning of one, attach them to the end in their
original ordering, and get the other string. Reordering the letters in some
other way does not, in general, produce a string that describes the same
necklace.

Write a function that returns whether two strings describe the same necklace.
'''


# Steps: 1: Verify that the set of letters is the same. Otherwise obviously
# there is no match, so easy elimination. 2: Inspect for conditions in premise.
# Slicing or rewriting to multiple strings/tuples to check for at least one 
# equivalency?

def same_necklace(str1,str2):
    '''
    Verify if two strings contain the same letters in the same order, 
    regardless of starting position. Input: two strings
    '''
    length = len(str1)
    
    #check obvious mismatches and matches
    if set(str1) != set(str2) or len(str1) != len(str2):
        return False
    elif str1 == str2:
        return True
    else:
        #try to match smallest common string
        for i in range(-1,-length-1,-1):
#            print(i)
            if str2.find(str1[0:i]) > -1:
                offset = str2.find(str1[0:i])
                found = str1[0:i]
                count = str2.count(found)
#                print('found: ',str1[0:i],'\noffset: ',str2.find(str1[0:i]),'\nlen-off: ',str1[length-offset::],'\ncount: ',count)
#                if not found:
#                    return False
#                if str2.find(str1[length-offset::]) == 0 and found:
#                    return True
                break
        
        
        if str2.find(str1[length-offset::]) == 0:
            return True
        #check for false negatives if multiple instances of smallest common string
        elif count > 1 and found:
            for i in range(count):
                offset2 = str2.find(found,offset+1)
#                print(offset2)
                if str2.find(str1[length-offset2::]) == 0:
                    return True
#    print(str1[length-offset::])

#    elif str2.find() > -1:
#        offset2 = str2.find(str1[length-offset::])
#    else:
    return False

        
#        
#test_str1 = 'nicoleni'
#test_str2 = 'colenini'
#test_str3 = 'incoleni'
#
#
#print(same_necklace(test_str1,test_str2))
#print(same_necklace(test_str1,test_str3))

print(same_necklace("aabaaaaabaab", "aabaabaabaaa")) #=> true
print(same_necklace("abc", "cba")) #=> false
print(same_necklace("xxyyy", "xxxyy")) #=> false
print(same_necklace("xyxxz", "xxyxz")) #=> false
print(same_necklace("x", "x")) #=> true
print(same_necklace("x", "xx")) #=> false
print(same_necklace("x", "")) #=> false
print(same_necklace("", "")) #=> true
