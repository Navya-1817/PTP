"""
recursive approach
tc: O(n)
sc: O(n) for recursion stack space
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        if not head:
            return None
        newhead = head
        if head.next:
            newhead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return newhead