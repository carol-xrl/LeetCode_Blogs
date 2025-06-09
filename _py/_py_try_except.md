用于处理异常
```python
try:
    num = int(input("请输入一个整数: "))
    result = 10 / num
except ValueError: print("输入的不是有效的整数！")
except ZeroDivisionError: print("不能除以0！") 
else: print("计算成功，结果为：", result) #无异常时
finally:
    # 无论成功与否，finally块都会执行，比如file.close()
```
常见error类型

| 错误类型              | 阐述                                        | 例子                         |
| ----------------- | ----------------------------------------- | -------------------------- |
| ValueError        | 表示传递给函数或操作的参数在值上是无效的，但类型是正确的。             | num = int("hello")         |
| TypeError         | 当操作或函数应用于错误类型的对象                          | "abc" + 123                |
| IndexError        | 在使用序列类型（如列表、元组、字符串）时，下标超出其范围而             | `lst = [1,2,3]`  `lst[5]`。 |
| KeyError          | 访问了字典中不存在的键                               |                            |
| ZeroDivisionError | /                                         | `1 / 0` 或 `10 % 0`         |
| EOFError          | 通常在没有更多输入而调用 `input()` 时出现，表示遇到文件或数据流的结束。 |                            |

例子
```python
try:
    with open("nonexistent_file.txt", "r") as f:
        data = f.read()
except FileNotFoundError as e:
    print("出现 FileNotFoundError:", e)
# e里是具体的报错信息
```