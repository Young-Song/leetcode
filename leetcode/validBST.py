# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.valid(root,-sys.maxint-1,sys.maxint) 
        
    def valid(self, root, left, right):
        if not root:
            return True
        if root.val<=left or root.val>=right:
            return False
        return self.valid(root.left,left,root.val) and self.valid(root.right,root.val,right)
        
