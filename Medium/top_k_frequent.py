"""
347. Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]

"""
from typing import List
import collections
import heapq
class Solution:
    #auto complete
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        The active selection is a Python code snippet that identifies the k most frequent elements in a list nums using a heap data structure. The process begins by creating a Counter object from the collections module, which counts the occurrences of each element in nums. This count is stored in the variable count and printed for debugging purposes.

        Next, the code constructs a list of tuples named heap, where each tuple consists of the negative count of an element and the element itself. The negative count is used to simulate a max-heap using Python's heapq module, which by default implements a min-heap. This transformation allows the most frequent elements to be at the top of the heap. The heap list is then printed to show its contents before heapification.

        The heapq.heapify(heap) function is called to convert the heap list into a valid heap in-place. This operation ensures that the heap properties are maintained, and the structure is printed again to show the state of the heap after heapification.

        Finally, the code extracts the k most frequent elements from the heap using a list comprehension. The heapq.heappop(heap) function removes and returns the smallest element from the heap, which corresponds to the most frequent element due to the negative counts. This operation is repeated k times, and the elements are collected into a list, which is then returned as the result. This list contains the k most frequent elements from the original nums list.
"""
        count = collections.Counter(nums)
        print(f"count {count}")
        heap = [(-value,key) for key,value in count.items()]
        print(f"heap {heap}")
        heapq.heapify(heap)
        print(f"heap after heapify {heap}")
         
        return [heapq.heappop(heap)[1] for _ in range(k)]


if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    k = 2
    res=Solution().topKFrequent(nums,k)
    print(f"res {res}")
    
    nums = [1]
    k = 1
    res= Solution().topKFrequent(nums,k)
    print(f"res {res}")

    nums = [1,1,1,2,2]
    k = 2
    res= Solution().topKFrequent(nums,k)
    print(f"res {res}")

    nums = [1,1,1,2,2,3,3,3,3]
    k = 2
    print(f"nums {nums}")
    res=Solution().topKFrequent(nums,k)
    print(f"res {res}")