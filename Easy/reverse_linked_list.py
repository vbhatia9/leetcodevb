"""
206. Reverse Linked List
"""
from typing import Optional

class ListNodevb:
    def __init__(self,val =0, next=None):
        self.val = val
        self.next = next
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
       