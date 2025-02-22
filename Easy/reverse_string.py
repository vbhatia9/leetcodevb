"""
344. Reverse String
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

"""
from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #not working in leetcode
        # x =s[::-1]
        # print(f"REVERSE is {x}")
        ####
        #Solution 1
        #The active selection is a snippet of Python code that reverses a sequence s in place. The code uses a for loop to iterate over the first half of the sequence. The loop variable i ranges from 0 to len(s)//2 - 1, where len(s) is the length of the sequence s. This ensures that the loop only runs for half the length of the sequence, which is sufficient for reversing it.
        #Within the loop, the code swaps the elements at positions i and ~i. The ~i expression uses the bitwise NOT operator, which in this context effectively computes the index from the end of the sequence. Specifically, ~i is equivalent to -i-1, so when i is 0, ~i is -1 (the last element), when i is 1, ~i is -2 (the second-to-last element), and so on. This swapping continues until the loop completes, resulting in the sequence being reversed.
        #The code then prints the reversed sequence s to the console.
        for i in range(len(s)//2):
            s[i], s[~i] = s[~i], s[i]
        print(f"REVERSE is {s}")

if __name__ == "__main__":
    s = ["h","e","l","l","o"]
    Solution().reverseString(s)
    s = ["H","a","n","n","a","h"]
    Solution().reverseString(s)