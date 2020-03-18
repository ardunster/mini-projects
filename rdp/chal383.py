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


from collections import Counter, defaultdict



def same_necklace(str1,str2):
    '''
    Verify if two strings contain the same letters in the same order, 
    regardless of starting position. Input: two strings
    '''
    length = len(str1)
    
    #check obvious mismatches and matches
    if str1 == str2:
        return True
    elif set(str1) != set(str2) or len(str1) != len(str2):
        return False
    
    for i in range(length):
        if str1 == (str2[i:] + str2[:i]):
            return True
        
    return False
        

#Tests:
#    
#test_str1 = 'nicoleni'
#test_str2 = 'colenini'
#test_str3 = 'incoleni'
#
#
#print(same_necklace(test_str1,test_str2)) # True
#print(same_necklace(test_str1,test_str3)) # False
#
#print(same_necklace("nicole", "icolen")) # => true
#print(same_necklace("nicole", "lenico")) # => true
#print(same_necklace("nicole", "coneli")) # => false
#print(same_necklace("aabaaaaabaab", "aabaabaabaaa")) #=> true
#print(same_necklace("abc", "cba")) #=> false
#print(same_necklace("xxyyy", "xxxyy")) #=> false
#print(same_necklace("xyxxz", "xxyxz")) #=> false
#print(same_necklace("x", "x")) #=> true
#print(same_necklace("x", "xx")) #=> false
#print(same_necklace("x", "")) #=> false
#print(same_necklace("", "")) #=> true
#
#print(same_necklace('abrades', 'sabered'))


# Bonus: identify the set of exactly 4 words in enable1.txt that describe the 
# same necklace.
    


with open("enable1.txt", "r") as f:
    enable1 = f.read().splitlines() 

d = defaultdict(list)

for i in enable1:
    id = tuple(sorted(tuple(Counter(i).items())))
    d[id].append(i)

m = defaultdict(list)

for k,v in d.items():
    if len(v) >= 4:
        for i in v:
            for j in v:
                if same_necklace(i,j) and i != j:
                    m[i].append(j)

for k,v in m.items():
    if len(v) >= 3:
        print(k,v)