"""
Products of Array Except Self
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in 
O
(
n
)
O(n) time without using the division operation?

Example 1:

Input: nums = [1,2,4,6]

Output: [48,24,12,8]
"""

def product_except_self(nums):
    n = len(nums)
    result = [1] * n

    # Calculate prefix products
    prefix = 1
    for i in range(n):
        result[i] = prefix # Store prefix product
        prefix *= nums[i] # Update prefix product
    # result[i] now contains the product of all elements to the left of nums[i]

    # Calculate suffix products and multiply with prefix
    suffix = 1
    for i in range(n - 1, -1, -1):# Traverse from right to left
        # result[i] already contains the prefix product
        # Now multiply it with the suffix product
        result[i] *= suffix
        suffix *= nums[i]

    return result

# Example usage
if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    print(product_except_self(nums))  # Output: [24, 12, 8, 6]