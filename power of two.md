### power of two
### 题意
给定一个整数，编写函数判断它是否是2的幂。
### 题解
如果一个整数是2的幂，那么它的二进制形式最高位为1，其余各位为0

等价于：n & (n - 1) = 0，且n > 0

### 代码
    class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        return n > 0 and n & (n - 1) == 0