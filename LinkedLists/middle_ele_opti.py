#using slow and fast pointer approach
#tc: O(n)
#sc: O(1)

class Solution:
    def middleNode(self, head) :
        slow = head
        fast = head
        while (fast!=None and fast.next!=None):
            slow = slow.next
            fast = fast.next.next
        return slow