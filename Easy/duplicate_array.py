
""" 217. Contains Duplicate 
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

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
#SOL 1
def dup(nums):
    hashset= set()
    for n in nums:
        if n in hashset:
            print("Contains Dup")
            return True
        else:
            hashset.add(n)
    return False

#SOL 2
def dup_set(nums):
    setList = set(nums)
    print(f"SETLIST {setList}")
    if len(setList) == len(nums):
            print("No Dup")
            return False
    else:   
            print("Contains Dup")
            return True  

if __name__ == "__main__":
    n = [1,3,4,5,9,1] # Dup value
    n = [1,3,4,5,9]
     
    print(f"calling Length {len(n)}")

   # sum_indx(n,target)
    #print(dup(n))
    print(dup_set(n))