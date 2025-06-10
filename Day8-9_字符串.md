---
title: Day8-字符串
tags: [LeetCode, 字符串]
categories: [Notes]
slug: 字符串
publish: true
---

# 基础
[py_string](_py/_py_string.md)
# 题目
## 反转字符串
[344题](https://leetcode.cn/problems/reverse-string/description/)
【我的解法 · range + 两两交换】
```python
class Solution(object):
    def reverseString(self, s):
        for i in range(int(len(s)/2)): # 可以写成len(s)//2 就不用int了
            s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]
        return 
```

【随想录 · 使用stack】怎么想到的？Stack的first in last out的特性很符合“反转”的需求
```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        stack = []
        for char in s:
            stack.append(char)
        for i in range(len(s)):
            s[i] = stack.pop()
```

【随想录 · 其他方法】
```python
s[:] = reversed(s)
s[:] = s[::-1]
s[:] = [s[i] for i in range(len(s) - 1, -1, -1)]
s.reverse()
```

注意：
【补充：Tuple Unpacking】
`s[i], s[j] = s[j], s[i]` 的执行顺序：
1. 先评估等号右侧，计算并创建一个 **临时元组** `(s[j], s[i])`。
2. 再unpacking赋值
避免额外使用变量，更简洁高效

【关于slice】
`s[:] = reversed_list` 修改的是s本身而不是创建新对象
`s = reversed_list` 只是修改s的引用，不会改变原来的s

【何时用库函数】
不涉及题的核心步骤且对其很了解（比如复杂度、底层实现）

## 反转字符串II
[541题](https://leetcode.cn/problems/reverse-string-ii/description/)
【我的解法 · 按题目条件分类讨论】
```python
class Solution(object):
    def reverseStr(self, s, k):
        s = list(s)
        n = len(s)//(2*k)
        if n >= 1:
            for i in range(n):
                s[i*k*2:i*k*2+k] = [s[j] for j in range(i*k*2+k-1,i*k*2-1,-1)]
        if len(s)%(2*k) == 0: return "".join(s)
        elif 0 < len(s)%(2*k) < k: s[n*k*2:] = [s[j] for j in range(len(s)-1,n*k*2-1,-1)]
        else: s[n*k*2:n*k*2+k] = [s[j] for j in range(n*k*2+k-1,n*k*2-1,-1)]
        return "".join(s)
```

【局部优化1】直接在 `range`里设置步长为 `2*k`，可以避免后续很多计算。
【局部优化2】利用`slice`的特性之\[1,2,3]\[1:1000] = \[1,2,3] 可以省去一些边界的判断。
【局部优化3】不需要用列表推公式，直接用slice。
优化版本：
```python
class Solution(object):
    def reverseStr(self, s, k):
        s = list(s)
        for i in range(0,len(s),2*k):
            s[i:i+k] = s[i:i+k][::-1]
        return "".join(s)
```
注意：
1. `str` 是不可以被修改的，所以需要转化成`list`再转化回去。
2. `str[(1,2,3)]` = `"(1,2,3,)"`, 因此要用`"".join(_str_name)`
3. 如何slice arr = \[1,2,3,4,5] 可以获得\[4,3,2,1]: 
```python
result1 = arr[3::-1] # O_s(K)
result2 = arr[:4][::-1] # # O_s(2K)
result3 = list(reversed(arr[:4])) # O_s(2K)reversed() 生成迭代器，需要用 list() 转换 
```

## 替换数字
[KamaCoder_54题](https://kamacoder.com/problempage.php?pid=1064)
【我的解法 · 转化成数组】$O_t(n)$ $O_s(n$) (python的list真好用，那就不看cpp双指针解法啦)
```python
def _convert_num():
    s = list(input())
    for i in range(len(s)):
        if s[i] in "1234567890":
            s[i] = "number"
    print("".join(s))
if __name__ == "__main__":
    _convert_num()
```
## 翻转字符串里的单词
[151题](https://leetcode.cn/problems/reverse-words-in-a-string/)
```python
class Solution(object):
    def reverseWords(self, s):
        return " ".join([ _ for _ in s.split()[::-1]])    
```
##  右旋转字符串
[Kamacoder_55题](https://kamacoder.com/problempage.php?pid=1065)
```python
def r_rvs():
    k, s = int(input()), input()
    print(s[-k:] + s[:-k])
if __name__ == "__main__":
    r_rvs()
```

## 实现 strStr( )
[28题](https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/description/)
【我的方法 · 暴力check（相当于两个for循环）】$O_t(mn)$
```python
class Solution(object):
    def strStr(self, haystack, needle):
        if (needle not in haystack): return -1
        for i in range(len(haystack)-len(needle)+1):
            if needle in haystack[i:i + len(needle)]: return i
```
【随想录 · index】

【随想录 · KMP算法】字符串匹配
前缀：包含首字母不包含尾字母的所有substring
后缀：包含尾字母不包含首字母的所有substring
最长相等前后缀：
## 重复的子字符串
[459题](https://leetcode.cn/problems/repeated-substring-pattern/description/)
【我的方法：暴力check】
```python
class Solution(object):
    def repeatedSubstringPattern(self, s):
        for i in range(1,len(s)//2+1):
            if s == s[:i]*(len(s)//i): return True
        return False
```


