"""
287. Find the Duplicate Number
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [3,3,3,3,3]
Output: 3
 

Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.
"""

def find_duplicate(nums):
    # Using Floyd's Tortoise and Hare (Cycle Detection)
    slow = nums[0]
    fast = nums[0]
    
    # Phase 1: Finding the intersection point of the two runners.
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    # Phase 2: Finding the entrance to the cycle.
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow

# Example usage:
print(find_duplicate([1,3,4,2,2]))  # Output: 2
print(find_duplicate([3,1,3,4,2]))  # Output: 3
print(find_duplicate([3,3,3,3,3]))  # Output: 3