# 基础
[py_hash](_py/_py_hash.md)
# 题目
## 有效的字母异位词
[242题](https://leetcode.cn/problems/valid-anagram/description/)
【我的方法：Counter】】$O_t(n)$  $O_s(m+n)$: 其中m, n 分别是s, t的长度。因为Counter是一个字典计算的时候需要分别对s、t的每一个字符进行储存。只考虑英文小写字母的话其实空间复杂度是$O(1)$, 但如果是Unicode则占用更多，是$O_s(n)$。

```python
class Solution(object):
    def isAnagram(self, s, t):
    # from collections import Counter
        return Counter(s) == Counter(t) 
```
【随想录 · 定一个长度为26的数组】$O_t(n)$  $O_s(1)$(因为定义的是一个常量大小的辅助数组) index为ord('s') - ord('a')。第一个string+1，第二个string-1，最后判断是否为0。
```python
class Solution(object):
    def isAnagram(self, s, t):
        list = [0]*26
        for i in s: list[ord(i) - ord("a")] += 1
        for i in t: list[ord(i) - ord("a")] -= 1
        for i in list:
            if i != 0: return False
        return True
```
【补充: [py_collections](py_collections)】
【补充: [py_内置函数](py_内置函数)】

## 两个数组的交集
[349题](https://leetcode.cn/problems/intersection-of-two-arrays/description/): 注意数据类型转化
```python
class Solution(object):
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))
```

## 快乐数
[202题](https://leetcode.cn/problems/happy-number/description/)
```python
class Solution(object):
    def isHappy(self, n):
        sum_set = set({})
        while True:
            sqr = 0
            for i in range(len(str(n))):
                sqr += int(str(n)[i])**2
            if sqr == 1: return True
            if sqr in sum_set: return False
            else: 
                sum_set.add(sqr)
                n = sqr
```

【随想录 · 精简写法】
```python
class Solution:
   def isHappy(self, n: int) -> bool:
       seen = set()
       while n != 1:
           n = sum(int(i) ** 2 for i in str(n))
           if n in seen:
               return False
           seen.add(n)
       return True
```
【语法: [_py_推导式](_py/_py_推导式.md)】

## 两数之和
[1题](https://leetcode.cn/problems/two-sum/description/) 
【我的方法 · 暴力】$O_t(N^2)$, $O_s(1)$ 
```python
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            cpl = target - nums[i]
            if cpl in nums[i+1:]: 
                return [i, nums.index(cpl, i+1)]
        return None
```
其实和这样写复杂度一样的：
```python
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
```

【代码随想录 · 字典】$O_t(N)$, $O_s(N)$ 由于我们不仅要知道元素是否有被遍历，还需要知道其对应的下标，因此使用dict。dict可以用key保存数值（判断是否出现过），用value再保存数值所在的下标（得到具体的下标）。
```python
class Solution(object):
    def twoSum(self, nums, target):
        dict_nums = {}
        for i in range(len(nums)): # 优化：使用enumerate
            if (target - nums[i]) not in dict_nums: # 用dict_nums.keys()会更慢
                dict_nums[nums[i]] = i
            else:
                return i, dict_nums[target - nums[i]]
        return False
```

## 四数相加II
[454题](https://leetcode.cn/problems/4sum-ii/description/)
【我的思路1 · 暴力4个for循环】$O_t(n^4)$ $O_s(1)$，正确但超时
【我的思路2 · 暴力优化2个循环】$O_t(n^2)$ $O_s(n^2)$，正确且不超时。想法是建立两个dictionary（因为可能会有相同和，所以用dict的value记录每种和的组合数），转化成两数相加的问题。
```python
lass Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        count = 0
        l = len(nums1)
        set1 = Counter(nums1[i] + nums2[j] for i in range(l) for j in range(l))
        set2 = Counter(nums3[i] + nums4[j] for i in range(l) for j in range(l))
        for i in set1:
            if (-i) in set2: # 用查询降低时间复杂度
                count += set1[i] * set2[-i]
        return count
```

## 赎金信
[383题](https://leetcode.cn/problems/ransom-note/description/)
【我的思路1 · Counter】$O_t(n)$ $O_s(n$) 
```python
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        dict_lt = Counter(magazine)
        for i in ransomNote:
            if dict_lt.get(i, 0) == 0: return False
            else: dict_lt[i] -= 1
        return True
```

【随想录 · Counter 的更优雅写法】
```python
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not Counter(ransomNote) - Counter(magazine)
""" Counter减法规则: 
A Counter({'d': 4, 'c': 3, 'b': 2, 'a': 1}) 
B Counter({'b': 3, 'a': 1}) 
A-B Counter({'d': 4, 'c': 3})
"""
```

【随想录 · 使用count】$O_t(n)$ $O_s(1)$ 很优雅！
```python
class Solution:
    def canConstruct(self, ransomNote, magazine):
        return all(ransomNote.count(c) <= magazine.count(c) for c in set(ransomNote))
```

【随想录 · 使用数组】$O_t(n)$ $O_s(1)$ (因为数组是一个长度为26的常量)
```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count = [0] * 26
        magazine_count = [0] * 26
        for c in ransomNote:
            ransom_count[ord(c) - ord('a')] += 1
        for c in magazine:
            magazine_count[ord(c) - ord('a')] += 1
        return all(ransom_count[i] <= magazine_count[i] for i in range(26))
```

## 三数之和
[15题](https://leetcode.cn/problems/3sum/description/)
【我的思路1 · 暴力3个for循环】正确但超时。
```python
class Solution(object):
    def threeSum(self, nums):
        count = set({})
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0: 
                        a = tuple(sorted([nums[i], nums[j], nums[k]])) # set里的元素必须immutable所以不可以是list（显然，如果是list则难判是否是相同元素）
                        count.add(a)
        return [list(i) for i in count] # 把tuple变回list
```
注意：
- `str([1,2]) = "[1,2]"` 
- `sorted(list_or_str_to_be_sorted)` 返回的是个list

【随想录 · 排序 + 双指针】$O(n log n) + O(n^2) = O(n^2)$
```python
class Solution(object):
    def threeSum(self, nums):
        _list = []
        nums = sorted(nums)
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums)-1
            while left < right:
                _sum = nums[i] + nums[left] + nums[right]
                if _sum == 0:
                    _list.append([nums[i], nums[left], nums[right]])
                    while left < right - 2 and nums[left] == nums[left+1]:
                        left += 1
                    while right > left and nums[right] == nums[right-1]:
                        right -=1
                    left, right = left+1, right-1
                elif _sum < 0:
                    left += 1
                else:
                    right -= 1
        return _list
```
- 要注意去重的细节，比如第一个指针应该是和`num[i]`和`nums[i-1]` 比，while时的条件
- 如何想到细节：Think step by step & 想一些特殊情况，如\[0,0,0,0,0,0,1,1,2\], \[-4,0,0,1,2,2,2,2,2,3], \[-5,-5,1,1,2,3,3,4,4,]

【随想录 · 字典】可以看下一道题

## 四数之和
[18题](https://leetcode.cn/problems/4sum/description/)
【我的思路1 · 两个双指针】$O_t(N^3)$ $O_s(k)$ 其中 `k` 是符合条件的四元组个数。一遍过，所有边界条件都被考虑到了 > \_< !
```python
class Solution(object):
    def fourSum(self, nums, target):
        _list = []
        nums = sorted(nums)
        for i in range(len(nums)-2):
	        # if nums[i] > target and nums[i] > 0: break 剪枝操作
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-1):
	            # if nums[i] + nums[j] > target and nums[j] > 0: break
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                left, right = j+1, len(nums)-1
                while left < right:
                    _sum = target - nums[i] - nums[j]
                    if nums[left] + nums[right] < _sum:
                        left += 1
                    elif nums[left] + nums[right] > _sum:
                        right -= 1
                    else:
                        _list.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left, right = left + 1, right - 1
        return _list    
```

【局部优化 · 剪枝】当nums\[i] > target，且nums\[i] > 0时后面的i都可不必检查；当nums\[i] + nums\[j] > target and nums\[j] > 0后面的j不必再被检查。有利于减少运行时间。

【补充】Short-circuit evaluation machanism
- 对于`while A and B` 如果A是False那么B不会执行
- 对于`while A or B` 如果A是True那么A不会执行
```python
a = False 
b = 1 / 0 # 不会导致 ZeroDivisionError
while a and b: print("不会执行这行")
```

【随想录 · 字典】$O_t(n^3)$， $O_s(n + k)$
```python
class Solution(object):
    def fourSum(self, nums, target):
        _frec = dict(Counter(nums))
        _result = set()
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                for m in range(j+1, len(nums)-1):
                    _cpm = target - nums[i] - nums[j] - nums[m]
                    # _count = sum([1 for _ in [nums[i], nums[j], nums[m]] if _ == _cpm]) 去掉sum的额外列表开销可以提升效率
                    _count = [nums[i], nums[j], nums[m]].count(_cpm)
                    if _cpm in _frec and _frec[_cpm] > _count:
                        _result.add(tuple(sorted([nums[i], nums[j], nums[m], _cpm])))
        return [list(_) for _ in _result]
```


