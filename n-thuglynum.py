# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 21:24:53 2015

@author: Understand
"""

def nthUglyNumber(n):
        """
        :type n: int
        :rtype: int
        """
        ugly= [1]
        
        i2 = i3 = i5 = 0
        next2 = 2
        next3 = 3
        next5 = 5
        
        while len(ugly) < n:
            next2, next3, next5 = ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5
            nextugly = min(next2, next3, next5)
            if nextugly == next2:
                i2 += 1
            if nextugly == next3:
                i3 += 1
            if nextugly == next5:
                i5 += 1
            ugly += nextugly,
        return ugly[-1]

print nthUglyNumber(10)
            
                