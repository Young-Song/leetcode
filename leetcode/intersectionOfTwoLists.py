# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # get two lists sizes
        m = 0
        cur = headA 
        while cur:
            m+=1
            cur=cur.next
        
        n = 0
        cur = headB
        while cur:
            n+=1
            cur=cur.next
            
        # suppose m>=n
        walk1 = headA # longer list
        walk2 = headB # shorter list
        
        # otherwise m<n    
        if m<n:
            walk1=headB
            walk2=headA
        
        diff= abs(m-n)
        
        for i in range(diff):
            walk1=walk1.next
        
        while walk1 and walk2:
            if walk1==walk2:
                return walk1
            walk1=walk1.next
            walk2=walk2.next
            
        return None
        
