```python
# 创建
set1 = {1, 2, 3, ‘4’}  
set2 = set([4, 5, 6, 7])
a = {x for x in 'abracadabra' if x not in 'abc'}
# 集合间运算符号 | - & ^, 返回值是set
# 其他操作
set1.add("5") # 添加
set1.update({key1:v1, key2:v2}) # 添加list/tuples/dicts(dict则是keys)的元素
set1.remove("2") # 删除该元素，不存在则报错
set1.discard("2") # 删除该元素，不存在不报错
x = set1.pop # 设置随机删除集合中的一个元素
length = len(set1) # 计算元素个数
set1.clear() # 清空集合，但集合仍然存在
"element" in set1 # 判断是否在集合里
```