# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        pre = root
        def pre_trv(root):
            if not root:
                return None
            nonlocal pre
            pre.right = root
            pre = root
            pre_trv(root.left)
            pre_trv(root.right)
        pre_trv(root.left if root.left else root.right)
        return root