# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
        
        # let node "run" proceed n steps first 
        idx = 0
        run = head
        
        # 
        while idx<n :
            idx+=1
            run=run.next
        cur = head    
        
        # move run and cur at the same time 
        while run and run.next:
            cur=cur.next
            run=run.next
        
        # if cur==head there are two possibilities 
        #   1) we want to remove the second node
        #   2) we want to remove the head node but we can't set cur to head's previous node
        
        # if run is None, we must delete head. 
        # The reason is run can only by None when we move run n times and n == list size
        if not run:
            head=head.next
            return head
        cur.next=cur.next.next
        
        return head
        
