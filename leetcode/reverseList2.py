# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        # set up tail
        tail = head
        t = 1
        while t<n:
            tail=tail.next
            t+=1
        # find the next node that not to be reversed            
        tailNext = tail.next 

        # set up head
        helper = ListNode(0)
        helper.next = head
        
        start = helper
        s = 1
        while s<m:
            start=start.next
            s+=1
        
        # reverse the middle
        prev = start
        cur = prev.next
        temp = cur
        nextNode = None
        while cur!=tailNext:
            nextNode = cur.next
            cur.next = prev
            prev= cur
            cur=nextNode
        start.next = prev
        temp.next= tailNext
        return helper.next
