---
title: Day3-4_链表
tags: [LeetCode, 链表]
categories: [Notes]
slug: 链表
publish: true
---

# 基础
[py_list](_py/_py_list.md)
[py_class](_py/_py_class.md)

# 题目
## 移除链表元素
[203题](https://leetcode.cn/problems/remove-linked-list-elements/): 删除链表中等于给定值 val 的所有节点。
示例 1： 输入：head = [1,2,6,3,4,5,6], val = 6 输出：[1,2,3,4,5]
示例 2： 输入：head = [], val = 1 输出：[]
示例 3： 输入：head = [7,7,7,7], val = 7 输出：[]
【我的思路】没有想到“虚拟头”的方式，于是用了两个while循环，一个用于移动head的位置确定新的头节点，一个用于修改其他元素。确定None/Null也专门写了判断条件，非常复杂。
【随想录解法：设置虚拟头】
```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        dummy_head = ListNode(next = head)
        cur = dummy_head
        while (cur.next != None):
            if cur.next.val == val:
                cur.next = cur.next.next
            else: cur = cur.next
        return dummy_head.next
```

## 设计链表
[707题](https://leetcode.cn/problems/design-linked-list/description/):
【我的思路】struggle with一些特殊条件（如head是none，index超出边界，index为0之类的）。很不优雅地使用了`try` - `excpet`
- **优化1**：引入成员 `size`，可以更好地 test validation of index而不是用 `try` - `excpet` 语句。
- **优化2**：把 `dummy_head` 作为`list`的成员。取消成员`head`, 用 `dummy_head.next` 来访问 `head` 且不用实时更新`head`。

```python
class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next
	
class MyLinkedList(object):
    def __init__(self):
        self.size = 0
        self.dummy_head = ListNode(next = None)
        
# 获取链表中下标为 index 的节点的值。如果下标无效，则返回 -1
    def get(self, index):
        # 先排除边界值
        if (index >= self.size) or (index < 0): return -1
        # 再移动到index位置
        cur = self.dummy_head.next
        for i in range(index):
                cur = cur.next
        return cur.val
	
# 将一个值为 val 的节点插入到链表中第一个元素之前。
    def addAtHead(self, val):
        self.dummy_head.next = ListNode(val, self.dummy_head.next)
        self.size += 1

# 将一个值为 val 的节点追加到链表中作为链表的最后一个元素。
    def addAtTail(self, val):
        cur = self.dummy_head
        for i in range(self.size):
            cur = cur.next
        cur.next = ListNode(val)
        self.size += 1

# 将一个值为 val 的节点插入到链表中下标为 index 的节点之前。如果 index 等于链表的长度，那么该节点会被追加到链表的末尾。如果 index 比长度更大，该节点将 不会插入 到链表中。
    def addAtIndex(self, index, val):
        if index < 0 or index > self.size: return
        cur = self.dummy_head
        for i in range(index):
            cur = cur.next
        cur.next = ListNode(val, cur.next)
        self.size += 1
        
# 如果下标有效，则删除链表中下标为 index 的节点。
    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size: return
        cur = self.dummy_head
        for i in range(index):
                cur = cur.next
        cur.next = cur.next.next
        self.size -= 1
```

## 反转链表
[206题](https://leetcode.cn/problems/reverse-linked-list/): 给单列表的`head`， 返回反转后的链表的`head`。
【我的思路】先用一个循环找到 `size`和 `tail`, 再一个一个反转。但不知道如何具体实现。要用递归，但自己并不熟练。
【随想录法1：双指针法】$O_t(n)$, $O_s(1)$。
```python
class Solution(object): #自己写的和答案一模一样！
    def reverseList(self, head):
        cur = head
        pre = None
        while cur is not None:
            next_pos = cur.next
            cur.next = pre
            pre = cur
            cur = next_pos
        return pre
```
【随想录法2：递归法】$O_t(n)$, $O_s(n)$
```python
# python 3.5+ 引入了type hinting
# 在函数def后面加 `->` 说明返回值的类型
# 在传入参数后面加 `:type` 说明
# 但如果真的出错不会报错
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        return self.reverse(head, None)
    def reverse(self, cur: ListNode, pre: ListNode) -> ListNode:
        if cur == None:
            return pre
        temp = cur.next
        cur.next = pre
        return self.reverse(temp, cur)
```

## 两两交换链表中的节点
[24题](https://leetcode.cn/problems/swap-nodes-in-pairs/description/)
【我的思路：写一个新函数递归】$O_s(n)$, $O_t(n)$。先考虑特殊情况，如果`head` 或`head.next` = `None` 则 `return head`。再设置一个 `dummy_head`。如果剩下的为大于零的偶数则翻转，以此往复。Leetcode过了，但略有一些冗余。
```python
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        if head == None or head.next == None: 
	        return head
        dummy_head = ListNode(next = head)
        cur = head
        pre = dummy_head
        self._reverse(cur, pre) # 记得用成员函数要加`self.`
        return dummy_head.next

    def _reverse(self, cur, pre):
	    # 由于我确保了第一次操作一定可以进行，所以把判断条件写在后面。
		# 交换操作
        pre.next = cur.next
        cur.next = cur.next.next
        pre.next.next = cur
        # 如果还可以继续操作，则进行递归操作。
        if cur.next == None: return
        if cur.next.next == None: return
        self._reverse(cur.next, cur) # 记得加`self.`
```

【随想录 · 优化之递归自己】$O_s(n)$, $O_t(n)$。不需要新写一个函数来递归，直接递归自己。且不需要`dummy_head`。（迭代很难很快的反应过来，关于返回值、边界值等等）
```python
class Solution:
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head
        # 待翻转的两个node分别是pre和cur
        pre = head
        cur = head.next
        next = head.next.next
        cur.next = pre  # 交换
        pre.next = self.swapPairs(next) # 将以next为head的后续链表两两交换
        return cur
```

【随想录 · 法2: 迭代 + 快慢指针】$O_s(1)$, $O_t(n)$。使用 `while` 循环。
```python
class Solution:
    def swapPairs(self, head):
        dummy_head = ListNode(next=head)
        cur = dummy_head
        # 必须有cur的下一个和下下个才能交换
        while cur.next and cur.next.next:
            temp = cur.next # 防止节点修改
            cur.next = temp.next
            temp.next = temp.next.next
            cur.next.next = temp
            cur = cur.next.next
        return dummy_head.next
```

## 删除链表的倒数第 N 个结点
[19题](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/)
【我的思路】先一个循环统计`size`, 再计算`idx`，然后删掉`idx`处的元素。
```python
class Solution(object):
    def removeNthFromEnd(self, head, n):
        size = 0
        cur = head
        # calculate the size
        while cur is not None:
            size += 1
            cur = cur.next
        idx = size - n
        # if idx invalid, do nothing
        if idx < 0 or idx >= size or size == 0: 
	        return head
        # delete the element with idx
        dummy_head = ListNode(next = head)
        pre = dummy_head
        for i in range(idx):
            pre = pre.next
        pre.next = pre.next.next
        return dummy_head.next
```

【随想录 · 快慢指针】$O_s(1)$, $O_t(n)$。`fast` 指针先前进 `n+1` 步，这样当 `fast` 走到 `None` 时，`slow` 正好在待删除节点的前一个节点。很新颖的思路！
```python
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(next = head)  # 创建虚拟头节点，防止删除头结点时出错
        fast = slow = dummy
        # fast 先走 n+1 步，使得 slow 指向待删除节点的前一个节点
        for _ in range(n + 1):
            fast = fast.next
        while fast:
            fast, slow = fast.next, slow.next
        slow.next = slow.next.next  # 删除目标节点
        return dummy.next  # 返回新链表的头结点
```
##  链表相交
[面试题02.07](https://leetcode.cn/problems/intersection-of-two-linked-lists-lcci/description/)
【我的思路】先计算两个列表的size，再用循环从后往前依次看一不一样，发现不一样的前一个node即为所求。（太复杂了就不写了）

【随想录 · 法一 ： 计算长度后对齐】先计算两个的长度，更长的那个往前移动长度的差值，然后一起移动。注意用了helper function的有效地复用了代码，别忘了对齐的位置以及`self.funtion_name`。
```python
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        size_A, size_B = self.size(headA), self.size(headB)
        cur_A, cur_B = (self.move_forward(headA, size_A - size_B), headB) if size_A > size_B else (headA, self.move_forward(headB, size_B - size_A))
        while cur_A and cur_B:
            if cur_A != cur_B:
                cur_A, cur_B = cur_A.next, cur_B.next
            else: 
                return cur_A
	
    def size(self, head):
            size, cur = 0, head
            while cur: # 不用写 `is not None`
                cur = cur.next
                size += 1
            return size
    
    def move_forward(self, head, step):
            for _ in range(step):
                head = head.next
            return head
    # 在函数里并不会改变实际head的指向
```

【补充语法 [py_传参](py_传参)】

【随想录 · 法二：等比例法】$O_s(1)$, $O_t(n)$。让两个指针分别遍历 `A` 和 `B`，并在到达 `None` 后，切换到另一个链表的头部，这样两个指针最终会在相交点处相遇（如果有交点），否则都会变成 `None`。长度一样但没交点的时候会在两个指针第一次到达尾部时返回`None`。
```python
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        ptrA, ptrB = headA, headB
        while ptrA != ptrB:
            ptrA = ptrA.next if ptrA else headB
            ptrB = ptrB.next if ptrB else headA
        return ptrA
```

发现要想到好方法，得经过一些观察，用一点点的数学知识🤔。

## 环形列表 II
[142题](https://leetcode.cn/problems/linked-list-cycle-ii/description/)
【我的思路：设list记录被访问过的元素】$O_t(n^2)$
```python
# Set
class Solution(object):
    def detectCycle(self, head):
        keeper = set({})
        while head:
            if head not in keeper:
                keeper.add(head)
                head = head.next
            else:
                return head
        return None
# Dictionary
class Solution(object):
    def detectCycle(self, head):
        keeper = {}
        while head:
            if head not in keeper:
                keeper[head] = True
                head = head.next
            else:
                return head
        return None

```
【语法补充：[_py_dict](_py/_py_dict.md) , [_py_set](_py/_py_set.md)】

【随想录 · 快慢指针法】$O_t(n)$
```python
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # If there is a cycle, the slow and fast pointers will eventually meet
            if slow == fast:
                # Move one of the pointers back to the start of the list
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        # If there is no cycle, return None
        return None
```