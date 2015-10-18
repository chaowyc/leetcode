# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 22:05:01 2015

@author: Understand
"""
import operator

def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
#        n = len(nums)
#        return n * (n + 1) / 2 - sum(nums)
    a = reduce(operator.xor, nums)
    print a
    b = reduce(operator.xor, range(len(nums) + 1))
    print b
    return a ^ b

print missingNumber([0, 1, 2, 4])