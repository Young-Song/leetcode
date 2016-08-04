# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return self.find(root,p,q)
        
    def find(self,root,p,q):
        if root==p or root==q:
            return root
        if not root:
            return None
        left = self.find(root.left,p,q)
        right= self.find(root.right,p,q)
        if left and right:
            return root
        if left :
            return left
        else:
            return right
            
