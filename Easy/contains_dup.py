"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element 
is distinct.

 217. Contains Duplicate

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

"""

from typing import List
#Solution 1
# In this approach, we convert the input list to a set and compare the lengths of the input list and the set.
# If the lengths are equal, it means that there are no duplicates in the input list, and we return False.
# Otherwise, we return True, indicating that there are duplicates in the input list.
# This approach has a time complexity of O(n) due to the set conversion and comparison operations.
# It is a simple and efficient solution to the problem.
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == len(set(nums)):
            return False
        else:
            return True

