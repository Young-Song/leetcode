# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result=[]
        elem=[]
        self.addElem(root,sum,elem,result)
        return result
        
    def addElem(self,root,sum,elem,result):
        if not root:
            return 
        if root.val==sum and not root.left and not root.right:
            elem.append(root.val)
            result.append(elem)
            return
        # store a copy of current elem list,
        temp =elem[:]
        new_sum = sum-root.val
        if root.left:
            elem.append(root.val)
            self.addElem(root.left,new_sum,elem,result)
            elem=temp
        if root.right:
            elem.append(root.val)
            self.addElem(root.right,new_sum,elem,result)
            elem=temp
