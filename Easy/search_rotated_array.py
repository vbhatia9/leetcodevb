"""
Search in Rotated Sorted Array
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) 
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, 
or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 """

def search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        #If nums[mid] is not the target, the function determines which side of 
        # the array is sorted. If the left side (nums[left] to nums[mid]) is sorted, it checks if the target lies within this range. If it does, it adjusts the right pointer to mid - 1 to search in the left half. Otherwise, it adjusts the left pointer to mid + 1 to search in the right half.

        if nums[left] <= nums[mid]: # left side is sorted
            if nums[left] <= target < nums[mid]:    # left side is sorted
                right = mid - 1
            else:
                left = mid + 1
        else:
            #If the right side (nums[mid] to nums[right]) is sorted, it checks if the target lies within this range.
            #  If it does, it adjusts the left pointer to mid + 1 to search in the right half. 
            # Otherwise, it adjusts the right pointer to mid - 1 to search in the left half.
            if nums[mid] < target <= nums[right]: # right side is sorted
                left = mid + 1
            else:
                right = mid - 1
    #If the target is not found within the loop, the function returns -1,
    #  indicating that the target is not present in the array.            
    return -1

# Example usage:

if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    target = 0
    print(search(nums, target))  # Output: 4