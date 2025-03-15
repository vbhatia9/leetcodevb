"""
3Sum
15. 3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.



"""
# Time complexity: O(n^2)
# Space complexity: O(1)
# Approach: We can sort the array and then use a two pointer approach to find the triplets. 
# We can fix one element and then use two pointers to find the other two elements. 
# We can keep track of the triplets and return the triplets at the end.
# The time complexity of this approach is O(n^2) and the space complexity is O(1).  
# The time complexity is O(n^2) because we are using a nested loop to find the triplets. 
# The space complexity is O(1) because we are not using any extra space.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
#AUTO
        nums.sort() # Sort the array to make it easier to avoid duplicates
        result = [] # Initialize an empty list to store the result
        n = len(nums)   # Get the length of the input array
        for i in range(n):  # Iterate through the array
            if i > 0 and nums[i] == nums[i - 1]:    # Skip duplicates   
                continue # Skip duplicate elements
            left, right = i + 1, n - 1 # Initialize two pointers
            while left < right:     # While the left pointer is less than the right pointer
                total = nums[i] + nums[left] + nums[right] # Calculate the sum of the three elements
                if total < 0: # If the sum is less than 0, move the left pointer to the right
                    left += 1 
                elif total > 0: # If the sum is greater than 0, move the right pointer to the left
                    right -= 1
                else:   # If the sum is equal to 0, add the triplet to the result list
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]: # Skip duplicates
                        left += 1   # Move the left pointer to the right
                    while left < right and nums[right] == nums[right - 1]:  # Skip duplicates
                        right -= 1  # Move the right pointer to the left
                    left += 1   # Move the left pointer to the right
                    right -= 1  # Move the right pointer to the left
        return result   # Return the result list
