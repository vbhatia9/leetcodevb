"""
128. Longest Consecutive Sequence
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. 
The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [2,20,4,10,3,4,5]

Output: 4
"""
from typing import List
# The problem asks us to find the length of the longest consecutive sequence of elements that can be formed from the given array. The elements do not have to be consecutive in the original array. We need to write an algorithm that runs in O(n) time. We can solve this problem using a hash set. The code for this approach is as follows:

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_streak = 0
        
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                longest_streak = max(longest_streak, current_streak)    

        return longest_streak
# Time complexity: O(n)
# Space complexity: O(n)
# Approach: We can build a set of the numbers in the array. For each number, we check if the number - 1 is not in the set. If it is not, then we can start a new streak from that number. We keep incrementing the number by 1 and checking if the next number is in the set. If it is, we increment the streak. We keep track of the longest streak and return
# the longest streak at the end.

# Another approach is to sort the array and then iterate through the array to find the longest consecutive sequence. This approach has a time complexity of O(nlogn) due to the sorting step. The space complexity is O(1) since we are not using any extra space. The code for this approach is as follows:
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:        
        if not nums:
            return 0
        
        nums.sort()
        longest_streak = 1
        current_streak = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1] + 1:
                    current_streak += 1
                else:
                    longest_streak = max(longest_streak, current_streak)
                    current_streak = 1
        
        return max(longest_streak, current_streak)
# Time complexity: O(nlogn) due to sorting
# Space complexity: O(1)        
# Approach: We sort the array and then iterate through the array to find the longest consecutive sequence. We keep track of the current streak and the longest streak. If the current number is equal to the previous number, we increment the current streak. If the current number is not equal to the previous number, we check if the current number is one greater than the previous number. If it is, we increment the current streak. If it is not, we update the longest streak and reset the current streak. We return the maximum of the longest streak and the current streak
# at the end.

# The first approach is more efficient as it has a time complexity of O(n) and a space complexity of O(n), while the second approach has a time complexity of O(nlogn) and a space complexity of O(1). The first approach is preferred for this problem.

