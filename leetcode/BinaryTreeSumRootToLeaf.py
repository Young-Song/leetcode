# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result=[0]
        self.addPathNum(root,result,0)
        return result[0]

    def addPathNum(self,root,result,cur):
        if not root:
            return
        if not root.left and not root.right:
            result[0]+=cur*10+root.val
        if root.left:
            self.addPathNum(root.left,result,cur*10+root.val)
        if root.right:
            self.addPathNum(root.right,result,cur*10+root.val)
            
            
