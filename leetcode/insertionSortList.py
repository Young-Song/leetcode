# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# may cause a TLE in Python 
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
            
        # sentinel
        helper = ListNode(0)
        prev=helper
        
        cur = head
        while cur:
            prev = helper
            nextNode = cur.next
            # test prev.next
            while prev.next and prev.next.val<=cur.val:
                prev=prev.next
            cur.next= prev.next
            prev.next=cur
            cur=nextNode
        return helper.next
