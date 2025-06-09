# sys.stdin
**`sys.stdin.readline()`**  
只读取一行字符串，即使文件有多行（包含换行符 `\n`，除非已到达 EOF）。若无输入/已到达文件末尾（EOF），则返回空字符串 `''`。
```python
import sys
line1 = sys.stdin.readline()
line2 = sys.stdin.readline()
print(f"第一行: {line1.strip()}")
print(f"第二行: {line2.strip()}")
```

**`sys.stdin.read([size])`**  
一次性读取 `size` 个字节（若不指定 `size` 或 `size` 为负数，则读取整个输入直到 EOF）。
```python
content = sys.stdin.read()
print(f"文件内容:\n{content}")
```

**`sys.stdin.readlines()`**  
一次性读取全部行并返回一个列表，每个元素是包含换行符的字符串。

```python
print("请输入多行内容（按 Ctrl+D 结束输入）：")
lines = sys.stdin.readlines()
print(f"读取的内容是:\n{lines}")
# 读取的内容是:
# ['Python\n', 'is\n', 'awesome!\n']
```
**直接迭代 `sys.stdin`**  
当你把 `sys.stdin` 当作可迭代对象时，会按行遍历输入。

```python
def process_stdin():
    for line in sys.stdin: #把sys.stdin当iterator，直到没有再下一行/interrupt时停止
        line = line.strip()  # 去掉\n, \t, 空格等
        if not line: # “”,[],0, None等会被视为False, 非空字符串/非空列表会被视为True
            continue # 即跳过没有内容的行
        print(f"Received: {line}")
```

# input()
相当于`sys.stdin.readline().strip()`

