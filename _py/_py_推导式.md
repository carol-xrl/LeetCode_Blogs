[参考：菜鸟教程](https://www.runoob.com/python3/python-comprehensions.html)
# 推导式
```python
# [list] 保留长度 > 3 的字符串并将它们大写
new_names = [name.upper()for name in names if len(name)>3]
# [dict] 创建有三个 (key, key*2) 元素的字典
dic = {x: x**2 for x in (2,3,4)}
# [集合]
a = {x for x in 'abracadabra' if x not in 'abc'}
# [元组]
a = (x for x in range(1,10)) 
# 但返回的是一个生成器对象, 如果需要元组类型需要写tuple(a)
```

- 创建一个 n\*n 的数组并初始化为0
【列表推导式】
```python
array = [[0]*n for _ in range(n)]
# 相当于
array = []
for i in range(n):
	array.append([0] * n)
# 以下语句会出错：
array = [[0] * 3] * 3
array[0][0] = 1
print(array) #[[1,0,0],[1,0,0],[1,0,0]]
```

# +聚合
```python
# 求阶乘和，可以改成min, max
from math import factorial 
n = sum(factorial(int(i)) for i in str(n))
# 求所有平方的乘积
from math import prod
n = prod(int(i) ** 2 for i in str(n))
# 按照平方值从小到大排序
list = sorted(int(i) ** 2 for i in str(n))
# 拼接字符串
"".join(str(int(i) * 2) for i in str(n))
```