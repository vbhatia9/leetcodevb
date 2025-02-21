"""
206. Reverse Linked List
"""
from typing import Optional
# Definition for singly-linked list.
class ListNodevb:
    def __init__(self,val =0, next=None):
        self.val = val
        self.next = next

#Solution 1
# In this approach, we use three pointers to reverse the linked list.
# We initialize the previous pointer to None, the current pointer to the head of the linked list, and the next pointer to None.
# We iterate through the linked list and update the next pointer of the current node to point to the previous node.
# We update the previous pointer to the current node and the current pointer to the next node.
# Finally, we return the previous pointer as the new head of the reversed linked list.
# This approach has a time complexity of O(n) since we iterate through each node in the linked list once.
# The space complexity is O(1) as we use a constant amount of extra space.
# This approach is efficient and easy to implement.
class Solution:
    def reverseList(self, head: Optional[ListNodevb]) -> Optional[ListNodevb]:
        previous = None # 1 -> 2 -> 3 -> 4 -> 5  => 5 -> 4 -> 3 -> 2 -> 1
        current = head
        while current:
            temp = current.next # 2 -> 3 -> 4 -> 5
            current.next = previous # 1 -> None
            previous = current # 1 -> None
            current = temp  # 2 -> 3 -> 4 -> 5
          
        return previous
    
if __name__ == "__main__":
    head = ListNodevb(1)
    head.next = ListNodevb(2)
    head.next.next = ListNodevb(3)
    head.next.next.next = ListNodevb(4)
    head.next.next.next.next = ListNodevb(5)
    
    obj1 = Solution()
    result = obj1.reverseList(head)
    while result:
        print(f"RES  VAL before {result.val}")
        result = result.next
        if result:
            print(f"RES  VAL after {result.val}")
       