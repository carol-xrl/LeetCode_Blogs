迭代的思路：
- 拆分成每一步的任务
- 确定终止条件、返回/打印值、特殊情况
```python
def jiecheng(n):
    if n == 0 or n == 1: return 1
    return n*jiecheng(n-1)
print(jiecheng(5)) # 120

def countdown(n):
    if n == 0: 
        print("End!")
        return
    print(n)
    countdown(n-1)
print(countdown(5)) # 5,4,3,2,1
```
