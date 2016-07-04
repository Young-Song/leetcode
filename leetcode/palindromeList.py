# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #O(n) time, O(1) space
        #reverse the second half and compare
        if not head:
            return True
        l = 0
        cur = head
        while cur:
            cur = cur.next
            l+=1
        half = l/2  
        middle = head
        while half>0:
            middle=middle.next
            half-=1
        # reverse half
        prev = None
        while middle:
            nextNode = middle.next
            middle.next=prev
            prev=middle
            middle=nextNode
        # if odd, there is one more node 
        newHalf=prev
        i = 0
        cur=head
        while i< l/2:
            if cur.val != newHalf.val:
                return False
            i+=1
            cur=cur.next
            newHalf=newHalf.next
        return True
