### nth ugly num
### 题目
编写程序寻找第n个“丑陋数” ugly number

丑陋数是指只包含质因子2, 3, 5的正整数。例如，1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前10个丑陋数。

注意，数字1也被视为丑陋数

### 题解
朴素的方法是对每一个数字重复调用isUgly方法，直到找到第n个为止。但是大部分数字都不是丑陋的。尝试寻找只生成丑陋数的方法

丑陋数必须由一个较小的丑陋数乘以2,3或者5得到

解决问题的关键是维护丑陋数的顺序。尝试一个类似于合并3个有序列表L1,L2与L3的方法

假设你当前计算出了第k个丑陋数Uk。则Uk+1一定是Min(L1 * 2, L2 * 3, L3 * 5)

解题思路：
参考：http://www.geeksforgeeks.org/ugly-numbers/

丑陋数序列可以拆分为下面3个子列表：
(1) 1×2, 2×2, 3×2, 4×2, 5×2, …
(2) 1×3, 2×3, 3×3, 4×3, 5×3, …
(3) 1×5, 2×5, 3×5, 4×5, 5×5, …
我们可以发现每一个子列表都是丑陋数本身(1, 2, 3, 4, 5, …) 乘以 2, 3, 5

接下来我们使用与归并排序相似的合并方法，从3个子列表中获取丑陋数。每一步我们从中选出最小的一个，然后向后移动一步。

代码：

    class Solution(object):
    def nthUglyNumber(self, n):
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


            
            
        