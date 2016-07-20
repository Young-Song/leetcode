# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        # find the middle node
        size = 0
        cur =head
        prev =None
        while cur:
            cur=cur.next
            size+=1
        mid = size/2
        cur = head
        while mid>0:
            prev=cur
            cur=cur.next
            mid-=1
        
        # if the size of the list is odd, move one node forward
        if size%2!=0:
            prev=prev.next
            cur=cur.next
        
        # cut the list into two parts
        prev.next = None
        
        #reverse the second half
        prev = None 
        nextNode = None
        while cur:
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur=nextNode
        # when returned, prev the the first node
        
        # interleave two lists
        l1 = head
        l2 = prev
        
        while l1 and l2:
            temp = l1.next
            temp2= l2.next
            l1.next=l2
            l2.next=temp
            l1 =temp
            l2 =temp2
        
        
    
        
