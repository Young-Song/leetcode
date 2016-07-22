# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        result=[]
        candidate=""
        self.findPath(root,result,candidate)
        return result
        
    def findPath(self,root,result,candidate):
        # null node
        if not root:
            return 
        
        # leaf node
        if not root.left and not root.right:
            candidate+= str(root.val)
            result.append(candidate)    
        
        candidate+= str(root.val)+"->"
        # recursive call on left and right
        if root.left:
            self.findPath(root.left,result,candidate)
        if root.right:
            self.findPath(root.right,result,candidate)
        return 
