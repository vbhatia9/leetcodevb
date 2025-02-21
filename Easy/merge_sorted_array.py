"""
88. Merge Sorted Array
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

"""

#Solution 1 mine
# In this approach, we iterate over the first array and compare each element with the first element of the second array.
# If the element in the first array is greater than the element in the second array, we swap the elements and sort the second array.
# We repeat this process until we reach the end of the first array. 
# This approach has a time complexity of O(n*mlogm), where n is the length of the first array and m is the length of the second array.
# The time complexity is dominated by the sorting operation on the second array after each swap.
# This approach is not optimal as it has a higher time complexity due to the sorting operation after each swap.
# It is better to use a more efficient approach that does not require sorting after each swap.
def merge_sorted_arrays(arr1, arr2):
    n, m = len(arr1), len(arr2)

    for i in range(n):
        if arr1[i] > arr2[0]:
            # Swap elements
            arr1[i], arr2[0] = arr2[0], arr1[i]
            arr2.sort()  # Sort the second array after each swap

# Solution 2 autopilot
# In this approach, we start from the end of the two arrays and compare the elements from the end to the beginning.
# We use two pointers, m and n, to keep track of the current index in nums1 and nums2, respectively.
# We compare the elements at indices m-1 and n-1 in nums1 and nums2, respectively.
# If the element at nums1[m-1] is greater than the element at nums2[n-1], we place the element at nums1[m-1] at the end of nums1 and decrement m by 1.
# Otherwise, we place the element at nums2[n-1] at the end of nums1 and decrement n by 1.
# We continue this process until we have processed all elements in nums1 and nums2.
# If there are remaining elements in nums2, we copy them to the beginning of nums1.
# This approach has a time complexity of O(m+n) since we iterate through all elements in nums1 and nums2 once.  
def merge(nums1, m, nums2, n):
    # Start from the end of nums1 and nums2
    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1
        else:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1
    
    # If there are remaining elements in nums2
    while n > 0:
        nums1[n - 1] = nums2[n - 1]
        n -= 1

if __name__ == "__main__": 
    arr1 = [1, 3, 5]
    arr2 = [2, 4, 6]
    merge_sorted_arrays(arr1, arr2)
    print(arr1)  # Output: [1, 2, 3]
    print(arr2)  # Output: [4, 5, 6]
