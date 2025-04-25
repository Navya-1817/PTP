""" using 3 vars 
tc: O(n)
sc: O(1)
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        prev,current=None, head
        while current:
            temp=current.next
            current.next=prev
            prev=current
            current=temp
        return prev