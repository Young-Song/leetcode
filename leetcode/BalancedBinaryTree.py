# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.balance(root)>=0
        
    def balance(self,root):
        if not root:
            return 0
        left = self.balance(root.left)
        right=self.balance(root.right)
        # if any subtree is invalid, immediately return false
        if left <0 or right<0:
            return -1
        # if the current node is unbalanced, return false
        if abs(left-right)>=2:
            return -1
        # return max depth
        return max(left,right)+1
