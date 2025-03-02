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

# author: leetcodevb
# Floyd's Tortoise and Hare (Cycle Detection)
# Time complexity: O(n)
# Space complexity: O(1)

"""
The active selection is a Python function named find_duplicate that identifies a duplicate number in a list nums using 
Floyd's Tortoise and Hare (Cycle Detection) algorithm. This algorithm is efficient and operates in O(n) time complexity 
with O(1) space complexity.

The function begins by initializing two pointers, slow and fast, both set to the first element of the list nums. 
These pointers are printed for debugging purposes to show their initial values.

In Phase 1, the function aims to find the intersection point of the two pointers. The slow pointer moves one step at a 
time (slow = nums[slow]), while the fast pointer moves two steps at a time ([fast = nums[nums[fast]]](http://vscodecontentref/8)). 
This phase continues until the slow and fast pointers meet, indicating the presence of a cycle. The values of slow and fast
are printed at each step to trace their movements.

In Phase 2, the function resets the slow pointer to the first element of the list and keeps the fast pointer at the 
intersection point found in Phase 1. Both pointers then move one step at a time (slow = nums[slow] and fast = nums[fast]) 
until they meet again. The point at which they meet is the entrance to the cycle, which corresponds to the duplicate number 
in the list. The values of slow and fast are printed at each step to trace their movements during this phase.

Finally, the function returns the value of the slow pointer, which is the duplicate number in the list. An example usage of 
the function is provided, where the input list [1, 3, 4, 2, 2] results in the output 2, indicating that 2 is the 
duplicate number in the list.

"""


def find_duplicate(nums):
    # Using Floyd's Tortoise and Hare (Cycle Detection)
    slow = nums[0]
    print(f"start slow {slow}")
    fast = nums[0]
    print(f"start fast {fast}")

    # Phase 1: Finding the intersection point of the two runners.
    while True:
        slow = nums[slow]
        print(f"slow {slow}")
        fast = nums[nums[fast]]
        print(f"fast {fast}")
        if slow == fast:
            break

    # Phase 2: Finding the entrance to the cycle.
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        print(f"slow line 51 {slow}")
        fast = nums[fast]
        print(f"fast line 53 {fast}")

    return slow


# Example usage:
print(find_duplicate([1, 3, 4, 2, 2]))  # Output: 2
# print(find_duplicate([3,1,3,4,2]))  # Output: 3
# print(find_duplicate([3,3,3,3,3]))  # Output: 3
