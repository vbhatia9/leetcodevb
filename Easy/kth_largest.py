"""
215. Kth Largest Element in an Array 

Find the k thlargest element in an unsorted array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 
"""

#Sol 1 autopilot  
# In this approach, we sort the array in ascending order and return the kth element from the end of the sorted array. 
# The time complexity of this approach is O(nlogn) due to the sorting operation.

def kth_largest(nums,k): 
    nums.sort() 
    return nums[-k]
#Sol 2
# In this approach, we use the nlargest function from the heapq module to find the kth largest element in the array.
# The nlargest function returns the k largest elements from the input list in descending order.
# We return the kth element from the nlargest output, which is the kth largest element in the array.
#time complexity of this approach is O(nlogk) due to the nlargest operation.
def kth_largest(nums,k): 
    import heapq 
    return heapq.nlargest(k,nums)[-1]

#Sol 3
# In this approach, we use a min-heap to keep track of the k largest elements in the array.
# We initialize a min-heap with the first k elements of nums.
# The heapq.heapify(min_heap) function transforms the first k elements of nums into a min-heap.
# The for loop iterates over the remaining elements in nums.
# If an element is larger than the smallest element in the heap (min_heap[0]), it replaces the smallest element to maintain the k largest elements in the heap.
# Finally, min_heap[0] returns the kth largest element.
# The time complexity of this approach is O(nlogk) due to the heapify and heappush operations.
def kth_largest(nums,k): 
    import heapq 
    heapq.heapify(nums) 
    return heapq.nlargest(k,nums)[-1]


#Sol 4 
# In this approach, we use a min-heap to keep track of the k largest elements in the array.
# We initialize a min-heap with the first k elements of nums.

# heapq.heapify(min_heap) transforms the first k elements of nums into a min-heap.
# The for loop iterates over the remaining elements in nums.
# If an element is larger than the smallest element in the heap (min_heap[0]), it replaces the smallest element to maintain the k largest elements in the heap.
# Finally, min_heap[0] returns the kth largest element.


import heapq

def kth_largest(nums, k):
    min_heap = nums[:k]
    heapq.heapify(min_heap)
    for num in nums[k:]:
        if num > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, num)
    return min_heap[0]

if __name__ == "__main__":
    nums = [3,2,1,5,6,4]
    k = 2
    print(kth_largest(nums,k))
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    print(kth_largest(nums,k))
    nums = [3,2,1,5,6,4]
    k = 2
    print(kth_largest(nums,k))
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4 



#Sol 5 mine
# In this approach, we use a min-heap to keep track of the k largest elements in the array.
# We initialize an empty min-heap.
# The for loop iterates over the elements in nums.
# We push each element into the min-heap.
# If the size of the min-heap exceeds k, we pop the smallest element from the heap.
# Finally, min_heap[0] returns the kth largest element.
# The time complexity of this approach is O(nlogk) due to the heap operations.
# The space complexity is O(k) to store the k largest elements in the heap.
import heapq

class findk():
    def find_k_largest(self,nums,k):
       # Use a min-heap to keep the top k largest elements
        min_heap = []

        for num in nums:
           
            print(f"Before MINHEAP {min_heap} and num is {num}")
            heapq.heappush(min_heap,num)
            print(f"After MINHEAP list {min_heap} and num is {num}")
            if len(min_heap)>k:
                heapq.heappop(min_heap)
                print(f"After popping MINHEAP list {min_heap}")
            
        print(f"{min_heap}")
        return min_heap[0]
    

if __name__ == "__main__":
   nums = [3, 2, 1,0,5, 6, 4]
   k = 2
   obj1 = findk()
   result = obj1.find_k_largest(nums,k)
   print("Kth Largest Element:", result)
    