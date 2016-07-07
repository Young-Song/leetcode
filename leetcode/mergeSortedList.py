# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        cur = result
        while l1 or l2:
            if not l1 and l2:
                cur.next = ListNode(l2.val)
                l2=l2.next
            elif not l2 and l1:
                cur.next = ListNode(l1.val)
                l1=l1.next
            else:
                if l1.val< l2.val:
                    cur.next=ListNode(l1.val)
                    l1=l1.next
                else:
                    cur.next=ListNode(l2.val)
                    l2=l2.next
            cur=cur.next
        
        return result.next
