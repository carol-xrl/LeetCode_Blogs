# 1. 一些术语
- 高度height：最下面的leaf是0，依次往上增加
- 深度depth：root是0，依次往下增加
# 2. 分类
- 满二叉树：除最后一层外degree都为0，最后一层都为leaves（若深度为k则有2^k -1个节点）
- 完全二叉树：除了最后一层外是满的，最后一层的node集中在左边（优先级队列是堆，堆是完全二叉树）
- 二叉搜索树：有数值，对于每一个节点，左子树若不为空，则左子树的所有节点均小于它的值；右，大。
	- 平衡二叉搜索树AVL：它是一颗空树或者它的左右两个子树的高度差的绝对值不超过1，左右子树也分别是AVL Tree（cpp中set, map, multimap, multiset的底层实现是AVL，unordered_map, unordered_set的底层实现是哈希表）
# 3. 储存方式
1. 链表，数组
```python
class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
```
# 4. 遍历方式：
- 深度优先遍历（借助stack）
    - 前序遍历（递归法，迭代法）
    - 中序遍历（递归法，迭代法）
    - 后序遍历（递归法，迭代法）
- 广度优先遍历（借助queue）
    - 层次遍历（迭代法）
![[IMG/Pasted image 20250320145911.png]]

|     | 增    | 删    |
| --- | ---- | ---- |
| AVL | logn | logn |
