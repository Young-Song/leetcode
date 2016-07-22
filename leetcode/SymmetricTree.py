# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.check(root.left,root.right)
    def check(self,first,second):
        if first and not second:
            return False
        if not first and second:
            return False
        if not first and not second:
            return True
        return first.val ==second.val and self.check(first.left,second.right) and self.check(first.right,second.left)
