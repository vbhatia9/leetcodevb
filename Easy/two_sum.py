"""1. Two Sum 

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
OR
Two SumGiven an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
Return the answer with the smaller index first.
 """

#Sol 2

def twosums(nums,target): 
    prevMap = {} #val : indx 
    for i , n in enumerate(nums): 
        print(f"I is {i},and Value is {n}") 
        diff = target - n 
        print(f"DIFF is {target}- {n} = {diff} ") 
        if diff in prevMap: 
            return (prevMap[diff],i) 
        prevMap[n]=i 
#Sol 1
def sum_indx(n,target): 
    output = [] 
    for i in range(0,len(n)): 
        for j in range(i+1,len(n)): 
            print(n[i],n[j]) 
            if n[i]+ n[j] == target: 
                output.append(i) 
                output.append(j) 
                print("output",output)

if __name__ == "__main__": 
    n = [1,3,4,5,9] 
    target = 7 
    print(f"calling Length {len(n)}") 
    # sum_indx(n,target) 
    print(twosums(n,target))