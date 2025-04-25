#what one would use to detect dupe in array-set
#as goining through cycle, we'll see the same node twice
# tc: O(n)
# sc: O(n) for set space

class Solution:
    def hasCycle(self, head) -> bool:
        Set = set()
        temp = head
        while temp:
            if temp in Set:
                return True
            Set.add(temp)
            temp = temp.next
        return False