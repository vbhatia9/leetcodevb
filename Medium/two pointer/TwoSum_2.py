"""
167. Two Sum II - Input Array Is Sorted
Medium
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
 

Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
"""
from typing import List

# Time complexity: O(n)
# Space complexity: O(1)
# Approach: We can use the two pointer approach to find the two numbers that add up to the target.
# We can initialize two pointers, one at the beginning of the array and one at the end of the array.
# We can keep moving the pointers until we find the two numbers that add up to the target.
# The time complexity of this approach is O(n) and the space complexity is O(1).
# The time complexity is O(n) because we are using a single loop to find the two numbers.
# The space complexity is O(1) because we are not using any extra space.
# The two pointer approach is an efficient way to solve this problem.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1 # Initialize two pointers
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]    # Return 1-indexed positions
             # Move the left pointer to the right or the right pointer to the left
            elif total < target:
                left += 1
            else:
                right -= 1
        return []

if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    print(solution.twoSum(numbers, target))
    # Output: [1, 2]
    numbers = [2, 3, 4]
    target = 6
    print(solution.twoSum(numbers, target))
    # Output: [1, 3]