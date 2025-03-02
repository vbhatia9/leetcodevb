"""
49. Group Anagrams
Given an array of strings strs, group the 
anagrams
 together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]
"""

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)
         
        for s in strs:
            count = [0] * 26 # a .... z
            #print(f"Count {count}")
            #print(f"s {s}")

            for c in s:
                #print(f"s {s} and C = {c}")
                count[ord(c)-ord('a')]+=1
                #print(f"NEW Count {count}")

            res[tuple(count)].append(s)
            #print(f"RES values {res.values()}  RES Items {res.items()}")
            print(f"RES values {list(res.values())} ")  
        return list(res.values())
    
    def groupAnagrams_v2(self, strs: list[str]) -> list[list[str]]:
        print("groupAnagrams_v2")
        print(f"STRS {strs}")
        res = defaultdict(list)

        for s in strs:
            print(f"String {s}")
            key = "".join(sorted(s))
            print(f"KEY {key}")

            res[key].append(s)
            print(f"RES values {list(res.values())} ")
            print(f"RES items {list(res.items())} \n*******")
        
        
        return list(res.values())

    
if __name__ == "__main__": 
    strs = ["eat","tea","tan","ate","nat","bat"]
   
    obj1 = Solution()
    print(f"Input {strs}")
    result = obj1.groupAnagrams(strs)
    print(f"Input {strs}")
    result = obj1.groupAnagrams_v2(strs)
