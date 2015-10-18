### Missing Number
### 题意
给定一个包含从0, 1, 2, ..., n, 选出的n个不同数字的数组，从中找出数组中缺失的那一个数。

例如，
给定 nums = [0, 1, 3] 返回2。
### 题解
1. 等差数列前n项和 - 数组之和
2. 位运算（异或运算）

### 代码
    class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return n * (n + 1) / 2 - sum(nums)


    class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = reduce(operator.xor, nums)
        b = reduce(operator.xor, range(len(nums) + 1))
        return a ^ b