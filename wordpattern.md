### word Pattern
### 题意
给定一个模式pattern和一个字符串str，判断str是否满足相同的pattern。

测试用例如题目描述。

pattern = "abba", str = "dog cat cat dog" should return true.

pattern = "abba", str = "dog cat cat fish" should return false.

pattern = "aaaa", str = "dog cat cat dog" should return false.

pattern = "abba", str = "dog dog dog dog" should return false.

### 题解
分别对pattern 和 word 建立字典

### code
    def wordPattern(pattern, str):
    	word = str.split()
    if len(pattern) != len(word):
        return False
    ptnDict = {}
    wordDict = {}
    for ptn, word in zip(pattern, word):
        if ptn not in ptnDict:
            ptnDict[ptn] = word
        if word not in wordDict:
            wordDict[word] = ptn
        if ptnDict[ptn] != word or wordDict[word] != ptn:
            return False
    return True