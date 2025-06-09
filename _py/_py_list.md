# 基本语法

| 方法                | 描述                                                                                                                         | 复杂度                        |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| list.append(x)    | 把一个元素添加到列表的结尾，相当于 a[len(a):] = [x]。                                                                                        | O(1)                       |
| list.extend(L)    | 通过添加指定列表的所有元素来扩充列表，相当于 a[len(a):] = L。                                                                                     | O(k)                       |
| list.insert(i, x) | 在指定位置插入一个元素。第一个参数是准备插入到其前面的那个元素的索引，例如 a.insert(0, x) 会插入到整个列表之前，而 a.insert(len(a), x) 相当于 a.append(x) 。                    | O(n)                       |
| list.remove(x)    | 删除列表中值为 x 的第一个元素。如果没有这样的元素，就会返回一个错误。                                                                                       | O(n)                       |
| list.pop([i])     | 从列表的指定位置移除元素，并将其返回。如果没有指定索引，a.pop()返回最后一个元素。元素随即从列表中被移除。（方法中 i 两边的方括号表示这个参数是可选的，而不是要求你输入一对方括号，你会经常在 Python 库参考手册中遇到这样的标记。） | 末尾:<br>O(1)<br>其他:<br>O(n) |
| list.clear()      | 移除列表中的所有项，等于del a[:]。                                                                                                      | O(n)                       |
| list.index(x)     | 返回列表中第一个值为 x 的元素的索引。如果没有匹配的元素就会返回一个错误。                                                                                     | O(n)                       |
| list.count(x)     | 返回 x 在列表中出现的次数。                                                                                                            | O(n)                       |
| list.sort()       | 对列表中的元素进行排序。                                                                                                               | O(nlogn)<br>Timesort       |
| list.reverse()    | 倒排列表中的元素。                                                                                                                  | O(n)                       |
| list.copy()       | 返回列表的浅复制，等于a[:]。                                                                                                           | O(n)                       |
# 栈
```python
class Stack:  
    def __init__(self):  
        self.stack = []  # “实例属性”，确保每个对象都有各自独立的列表
        # 和公开变量不同，前者是“类属性”所有对象共享这一份列表。
        # stack 也可以写成其他种种
    def push(self, item):  
        self.stack.append(item)  
  
    def pop(self):  
        if not self.is_empty():  
            return self.stack.pop()  
        else:  
            raise IndexError("pop from empty stack") 
            # 表示主动抛出一个IndexError异常，并且附带一个错误提示信息
  
    def peek(self):  # 查看栈顶元素
        if not self.is_empty():  
            return self.stack[-1]  
        else:  
            raise IndexError("peek from empty stack")  
  
    def is_empty(self):  
        return len(self.stack) == 0  
  
    def size(self):  
        return len(self.stack)  
  
# 使用示例  
stack = Stack()  
stack.push(1)  
stack.push(2)  
stack.push(3)  
print("栈顶元素:", stack.peek())  # 输出: 栈顶元素: 3  
print("栈大小:", stack.size())    # 输出: 栈大小: 3  
print("弹出元素:", stack.pop())  # 输出: 弹出元素: 3  
print("栈是否为空:", stack.is_empty())  # 输出: 栈是否为空: False  
```

# Queue
法一：用deque: 它是双端队列，可以在两端搞高效添加和删除元素$O_t(1)$。
评价：deque和list的好坏
- 若需要**随机访问**（如频繁地用 `d[i]` 访问任意位置），`deque` 并不合适，索引访问最坏可达 **O(n)**；在这方面，传统的 Python `list`（动态数组）才是直接 O(1) 的随机访问。
- 若需要的是**高速的双端操作**（如实现队列、实现滑动窗口等），`deque` 会比 `list` 更合适。

| 语句                                             | 解释         | 复杂度                                     |
| ---------------------------------------------- | ---------- | --------------------------------------- |
| append(x)/appendleft(x)                        | 在右/左端添加    | O(1)                                    |
| pop()/popleft()                                | 从右/左端弹出    | O(1)                                    |
| extend(iterable)/extendleft(iterable)          | 从右/作左端批量添加 | **O(k)**，其中 _k_ 是要添加的元素个数，坐断添加时添加顺序会被反转 |
| **访问末端元素**（如 `d[0]`, `d[-1]`）                  |            | O(1)                                    |
| 访问任意位置 `d[i]`, `remove(value)`, `in` , `count` |            | 最坏情况下为 **O(n)**                         |

```python
class MyQueue(object):
    from collections import deque
    def __init__(self):
        self.queue = deque()
    def push(self, x):
        self.queue.append(x)
    def pop(self):
        if len(self.queue) != 0:
            return self.queue.popleft()
        else:
            raise IndexError("pop from an empty queue")
    # 返回队列开头的元素
    def peek(self):
        if len(self.queue) != 0:
            return self.queue[0]
        else:
            raise IndexError("peek an empty queue")
    def empty(self):
        return len(self.queue) == 0
```

法二：用list
```python
class Queue:  
    def __init__(self):  
        self.queue = []  
  
    def enqueue(self, item):  
        self.queue.append(item)  
  
    def dequeue(self):  
        if not self.is_empty():  
            return self.queue.pop(0)  
        else:  
            raise IndexError("dequeue from empty queue")  
  
    def peek(self):  
        if not self.is_empty():  
            return self.queue[0]  
        else:  
            raise IndexError("peek from empty queue")  
  
    def is_empty(self):  
        return len(self.queue) == 0  
  
    def size(self):  
        return len(self.queue)  
  
# 使用示例  
queue = Queue()  
queue.enqueue('a')  
queue.enqueue('b')  
queue.enqueue('c')  
print("队首元素:", queue.peek())    # 输出: 队首元素: a  
print("队列大小:", queue.size())    # 输出: 队列大小: 3  
print("移除的元素:", queue.dequeue())  # 输出: 移除的元素: a  
print("队列是否为空:", queue.is_empty())  # 输出: 队列是否为空: False

```
# 链表
```python
class ListNode:
    def __init__(self, val=0, next=None):
	    # 这些是实例属性，不是类属性
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None  # 头结点初始化为空

    def append(self, val):
        """在链表**末尾**添加一个节点"""
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        """打印链表"""
        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

# 示例
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.print_list()  # 输出: 1 -> 2 -> 3 -> None
```