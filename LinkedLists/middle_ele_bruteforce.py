#first getting total count of nodes
#traversing upto count//2 and returning that node
#tc: O(n)
#sc: O(1)

class Solution:
    def middleNode(self, head):
        count = 0
        nexto = head
        while nexto:
            count += 1
            nexto = nexto.next
        
        i=0
        nexto = head
        while(i<count//2):
            nexto = nexto.next
            i+=1
        return nexto