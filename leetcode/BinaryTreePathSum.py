# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        return self.findSum(root,sum)
        
    def findSum(self,root,sum):
        """
        if not root:
            if sum==0:
                return True
            else:
                return False
        """
        # NOTE we have to chekc the leave nodes
        if not root.left and not root.right:
            return sum==root.val
        left=False
        right =False
        if root.left:
            left=self.findSum(root.left,sum-root.val)
        if root.right:
            right=self.findSum(root.right,sum-root.val)
        return left or right
