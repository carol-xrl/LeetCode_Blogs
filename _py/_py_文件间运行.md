每个模块都有一个内置变量 `__name__`。当你直接运行一个 Python 脚本时，解释器会把该脚本的 `__name__` 变量设置为 `"__main__"`；而如果这个文件被当作模块导入到其他脚本中时，`__name__` 的值则是该模块的名字（即文件名，不包含扩展名）。

```python
def main():
    print("Hello, world!")

def helper():
    print("This is a helper function.")

if __name__ == "__main__":
    main()

```

- 如果你在命令行中运行 `python example.py`，此时 `__name__` 的值为 `"__main__"`，所以会调用 `main()` 函数，输出 `Hello, world!`。
- 如果你在另一个文件中写 `import example`，那么 `__name__` 的值为 `"example"`，`if` 语句条件不成立，`main()` 函数不会被自动调用；这样你可以选择性地使用 `example` 模块中的其他函数，比如调用 `example.helper()`。
