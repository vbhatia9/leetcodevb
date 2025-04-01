# Definition for singly-linked list.
""" 
21. Merge Two Sorted Lists"
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
 
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        current = dummy
        
        while l1 and l2: # While both lists are not empty
            # Compare the values of the two nodes
            # and append the smaller one to the merged list
            # Move the pointer of the list from which the node was taken
            # to the next node
            # Append the smaller node to the merged list
            # Move the pointer of the merged list to the next node
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        
        if l1:
            current.next = l1 # If there are remaining nodes in l1, append them
        # If there are remaining nodes in l2, append them
        elif l2:
            current.next = l2
        
        return dummy.next