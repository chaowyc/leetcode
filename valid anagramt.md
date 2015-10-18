### valid Anagram
### 题意
给定字符串s和t，编写函数判断t是否为s的anagram（字谜游戏，由颠倒字母顺序而构成的字[短语]）。

### 题解
1. 排序
2. 哈希表

### 代码
    class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)
       
    def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    #return sorted(s) == sorted(t)
    from collections import Counter
    return Counter(s).items() == Counter(t).items()
    
	print isAnagram("anagram", "nagaarm")