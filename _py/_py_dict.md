[参考：菜鸟教程](https://www.runoob.com/python/att-dictionary-cmp.html)
```python
tinydict = {'Name': 'Zara', 'Age': 7, 'Class': 1} # create
tinydict['Age'] = 8 # 更新
tinydict['School'] = "RUNOOB" # 添加
len(tinydict) # 计算dict中的keys总数
del tinydict['Name'] # 删除键是'Name'的条目 
tinydict.clear() # 清空字典所有条目 
del tinydict # 删除字典
pop(key[,default]) 
# - 如果 `key` 存在 - 删除字典中对应的元素并返回
# - 如果 `key` 不存在且设置了default - 返回设置指定的默认值
# - 如果 `key` 不存在且default未指定 - 触发KeyError
popitem() # 返回并删除字典中的最后一对键和值。若字典为空，则KeyError
len(dict) # 计算字典keys总数
type(dict) # 返回类型，即dict
dict.copy # 返回字典的浅拷贝.直接复制 dict2 = dict1 则是完全引用
dict.items() #以list返回可遍历的(key, value)元组list
dict.keys() # 以list返回所有keys
dict.values() # 以list返回所有values
print(tinydict['Age']) # 访问字典某个元素
'a' in tinydict #判断是否在key中
'a' in tinydict_keys() # 同上，但更慢，因为要额外创建dict_keys视图
s = dict1.get('Salary', 0.0) # 如果key不在dict中则返回None或设置的默认值（比如这里是0.0）。比起直接使用dict1['Salary']，不会触发KeyError
name = ['a', 'b', 'c']
dict1 = dict.fromkeys(name, 'UIUC') 
print ("the name list is: %s" % str(dict1)) 
# str(dict): 输出字典可打印的字符串表示：
# the name list is: {'a': 'UIUC', 'b': 'UIUC', 'c': 'UIUC'} 
# dict_name.fromkeys(seq[, value])以序列 seq 中元素做字典的键，value 为字典所有键对应的初始值,value可以没有的默认值是None
dict.update(dict2) # 把字典 dict2 的键/值对更新到 dict 里。
```

注意：
- dict 作为 Python 的关键字和内置函数，变量名不建议命名为 **dict**。
- key必须immutable(string, int, float, tuple)，list不能做keys。

## defaultdict
```python
from collections import defaultdict 
class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        rec, cnt = defaultdict(lambda : 0), 0
        for i in nums1:
            for j in nums2:
                rec[i+j] += 1
        for i in nums3:
            for j in nums4:
                cnt += rec.get(-(i+j), 0) 
        return cnt
```

## Counter
```python
from collections import Counter
nums = [1, 2, 2, 3, 3, 3]
counter = Counter(nums)
print(counter) # 输出：Counter({3: 3, 2: 2, 1: 1})
counter['a']  # 返回字符 'a' 出现的次数。若不存在，默认返回0.
counter.most_common(2)  
# 输出：[('a', 3), ('n', 2)]，前两个最常见的元素
for key, count in counter.items():
    print(f"{key}: 出现了 {count} 次")
c1 = Counter("hello")
c2 = Counter("world")

print(c1 + c2)  # 频率相加
print(c1 - c2)  # 频率相减（负数会被去掉）

dict(counter)  # 转为普通字典
list(counter.elements())  
# → ['b', 'a', 'a', 'a', 'n', 'n']
# 根据计数重复元素
```
