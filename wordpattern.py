# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 00:47:37 2015

@author: Understand
"""

#def wordPattern(pattern, str):
#    word = str.split()
#    if len(pattern) != len(word):
#        return False
#    ptnDict = {}
#    wordDict = {}
#    for ptn, word in zip(pattern, word):
#        if ptn not in ptnDict:
#            ptnDict[ptn] = word
#        if word not in wordDict:
#            wordDict[word] = ptn
#        if ptnDict[ptn] != word or wordDict[word] != ptn:
#            return False
#    return True
#def wordPattern(pattern, str):
#    s = pattern
#    t = str.split()
#
#    return map(s.find, s) == map(t.index, t)

def wordPattern(pattern, str):
    s = pattern
    t = str.split()
    return len(set(zip(s, t))) == len(set(s)) == len(set(t)) and len(s) == len(t)
    

print wordPattern("abba", "cat dog dog cat")



    


    