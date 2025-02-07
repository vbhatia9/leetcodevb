"""
Problem: Kth Largest Element in an Array
Find the k thlargest element in an unsorted array.
Note that it is the k th
  largest element in sorted order, not the k th
  distinct element
nums = [3, 2, 1, 5, 6, 4], k = 2
"""
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
    