#using slow and fast pointers
#tc: O(n)
#sc: O(1)


class Solution:
    def hasCycle(self, head) -> bool:
        slow = head
        fast = head
        while fast!=None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                return True
        return False