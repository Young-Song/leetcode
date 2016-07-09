# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        cur=result
        carry = 0
        while carry or l1 or l2:
            digit = 0
            if carry ==1:
                digit+=1
            if l1:
                digit+=l1.val
                l1=l1.next
            if l2:
                digit+=l2.val
                l2=l2.next
            carry = digit/10
            digit= digit%10
            cur.next=ListNode(digit)
            cur=cur.next
        return result.next
        
            
