"""
125. Valid Palindrome
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Sol 1
        # s = ''.join(filter(str.isalnum, s)).lower()
        # return s == s[::-1]
       
    
   
        #Sol 2
        # newstr = ""
        # for c in s:
        #     if  c.isalnum():
        #        newstr += c.lower() 
        # print(newstr)
        # return newstr == newstr[::-1]
    
        



       #Sol 3
       #left pointer and right pointer
         #left pointer will move from left to right 
            #right pointer will move from right to left
        l ,r = 0,len(s)-1
        while l<r:
            if not s[l].isalnum():
                l+=1
            elif not s[r].isalnum():
                r-=1
            elif s[l].lower() != s[r].lower():
                return False
            else:
                l+=1
                r-=1
        return True
        #Time complexity is O(n) and space complexity is O(1)
        

    
if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    obj1 = Solution()
    result = obj1.isPalindrome(s)   
    print(result)
    s2 = "race a car"
    result = obj1.isPalindrome(s2)   
    print(result)