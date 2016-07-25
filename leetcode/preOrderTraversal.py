# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
            
        stack = []
        cur = root
        result=[]
        while stack or cur:
            if cur :
                result.append(cur.val)
                stack.append(cur)
                cur=cur.left
            else:
                cur=stack.pop()
                cur=cur.right
        return result
