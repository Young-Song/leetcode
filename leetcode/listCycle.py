# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if not head:
            return False
        cur = head
        n = cur.next
        while n and n.next:
            cur=cur.next
            n=n.next.next
            if cur==n:
                return True
                
        return False
        
