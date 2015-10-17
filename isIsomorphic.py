# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 01:28:42 2015

@author: Understand
"""

#def isIsomorphic(s, t):
#    if len(s) != len(t):
#        return False
#    sDict = {}
#    tDict = {}
#    for i, j in zip(s, t):
#        if i not in sDict:
#            sDict[i] = j
#        if j not in tDict:
#            tDict[j] = i
#        if sDict[i] != j or tDict[j] != i:
#            return False
#    return True

#def isIsomorphic(s, t):
#    return map(s.find, s) == map(t.find, t)
#
def isIsomorphic(s, t):
    return len(set(zip(s, t))) == len(set(zip(s, t))) and len(s) == len(t)    
print isIsomorphic("add", "egg")

