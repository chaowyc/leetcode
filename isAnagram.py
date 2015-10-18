# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 22:40:41 2015

@author: Understand
"""

def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    #return sorted(s) == sorted(t)
    from collections import Counter
    return Counter(s).items() == Counter(t).items()
    
print isAnagram("", "")