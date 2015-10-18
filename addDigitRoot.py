# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 20:03:44 2015

@author: Understand
"""

def addDigitRoot(num):
    if num == 0:
        return 0
    return (num - 1) % 9 + 1