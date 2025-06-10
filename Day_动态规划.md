---
title: Day_动态规划
tags: [LeetCode, 动态规划]
categories: [Notes]
slug: 动态规划
publish: true
---

# 理论

# 题目
## 斐波那契数
[509_ez](https://leetcode.cn/problems/fibonacci-number/description/)
【我的思路1 · 递归】$O_t(2^n)$ $O_s(n)$
- 虽然可以过leetcode，但时间复杂度爆炸
- （疑似二叉树的时候写魔怔了）
```python
class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1: 
	        return n
        return self.fib(n-1) + self.fib(n-2)
```
【我的思路2 · 迭代】$O_t(n)$ $O_s(1)$
```python
class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1: 
	        return n
        pre_2, pre_1 = 0, 1
        for i in range(2, n + 1):
            pre_2, pre_1 = pre_1, pre_2 + pre_1
        return pre_1
```
【随想录 · dp标准写法】
- 其实和上面一样，只是想借此感受一下dp的思想。
```python
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1: return n # 排除corner case
        dp = [0, 1] # 构建dp table并初始化
        for _ in range(2, n+1): # 用转移公式遍历
            dp[0], dp[1] = dp[1], dp[0] + dp[1]
        return dp[1] # 返回答案
```
【变式 · 爬楼梯】[70_ez](https://leetcode.cn/problems/climbing-stairs/submissions/619151787/)只是换个说法。
【变式 · 打家劫舍】 [198_md](https://leetcode.cn/problems/house-robber/description/) 只是多增加了一个条件。
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length <= 2:
            return max(nums)
        nums[2] = nums[2] + nums[0]
        for i in range(3,len(nums)):
            nums[i] += max(nums[i-2], nums[i-3])
        return max(nums[length-1], nums[length-2])
```
## 最长递增子序列
[300_md](https://leetcode.cn/problems/longest-increasing-subsequence/description/)
【我的思路1】：$O_t(n^2)$ 
- `dp[i]` 表示以 `nums[i]` 结尾的最长上升子序列长度。
- 转移方程（计算以该字符结尾的最长递增序列）：`dp[i] = max(dp[1], dp[j] + 1 for j < i and nums[j] < nums[i])`
```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [1] * length
        for i in range(1, length):
            for j in range(i-1, -1, -1):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)      
```
## 最长公共子序列
[1143_md](https://leetcode.cn/problems/longest-common-subsequence/)
【我的思路1】
- dp\[i]\[j] 表示序列1\[0: i+1]以及序列2\[0:j+1] 的最长子序列，初始化为0。
- 转移方程：固定下来序列1的前i个元素，最长序列长度为下两者的max：
	- 以它结尾的序列（对序列2从后往前遍历发现在第k个，那么长度就是dp\[i-1, k-1] + 1）
	- 不以它结尾的序列，即dp\[i-1, j]）
- 边角情况：序列1的第一个元素时需要访问dp\[i-1, k-1]或dp\[i, j-1] & dp\[i-1, j-1]从而导致index error。所以可以把数组加以个“左上边框”，第一列&第一排的元素为0。这样可以统一写法。
```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1, len2 = len(text1), len(text2)
        dp = [[0]*(len2 + 1) for _ in range(len1 + 1)]
        for i in range(1,len1+1):
            for j in range(1, len2+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return dp[len1][len2]

```
- 注意数组的横竖。
- 注意，构建数组我们用推导式而非`[[0]*len2]*len1`构建。详见[_py_basics](_py/_py_basics.md) 里shallow/copy讲解。

# 单词拆分
[139_md](https://leetcode.cn/problems/word-break/description/)
- 刚开始没有想出来很简单的方法，以下是inspired by GPT写的。
- 状态：`dp[i]` 表示前 `i` 个字符是否可以被字典拼出来。被初始化为False。
- 转移方程：`dp[i] = any(dp[j] and s[j:i] in wordDict for j in range(i))` 
- 边角情况：第一个元素的检查会被跳过，从而如果第一个元素存在字典中还是是False。所以把数组长度+1，然后第一个元素变成True。
- 降低复杂度：dict改set。因为`a in set`是O(1), `a in list`是O(n)
```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        length = len(s)
        wordset = set(wordDict)
        dp = [False]*(length+1)
        dp[0] = True
        for i in range(1,length+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordset:
                    dp[i] = True
                    break 
        return dp[-1]
```

## 最小路径和
[64_md](https://leetcode.cn/problems/minimum-path-sum/description/)
【我的思路1】
- 状态`dp[i][j]`表示到元素的最小距离
- 一个状态取决于其上或左格的状态（有些边界的地方没有）。
- 遍历顺序，就是按照下标和一样的情况，从右上角到左下角遍历。
- 转移方程，min(左格{如果有的话}+自己，上格{如果有的话}+自己)
- 边角条件：左、上格可能没有，那么可以在最上面增加一行，最左边增加一行，初始化为0.
```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        l, h = len(grid), len(grid[0])
        print(l,h)
        dp = [[float("inf")]*(h+1) for _ in range(l+1)]
        for i in range(l):
            for j in range(h):
                dp[i+1][j+1] = grid[i][j]
        for i in range(3, l+h+1):
            for j in range(min(h,i-1), max(1,i-l)-1, -1):
                dp[i-j][j] = min(dp[i-j-1][j], dp[i-j][j-1]) + dp[i-j][j]
        return dp[l][h]
```

【优化】
- 边角条件的处理不一定要
其他建议的题70 + 746 + 416 + 62 + 63

# 心得
