"""
13. Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].

"""
#   Solution 1
# In this approach, we use a dictionary to map the Roman numerals to their corresponding integer values.
# We iterate through the input string s and compare the values of the current Roman numeral and the next Roman numeral.
# If the value of the current Roman numeral is less than the value of the next Roman numeral, we subtract the value of the 
# current Roman numeral from the total.
# Otherwise, we add the value of the current Roman numeral to the total.
# Finally, we return the total value as the result.
# This approach has a time complexity of O(n) since we iterate through the input string s once.
# The space complexity is O(1) as we use a fixed-size dictionary to store the Roman numerals and their corresponding values.
# This approach is efficient and easy to implement.

class Solution:
    def romanToInt(self, s: str) -> int:
        roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        number=0
        for i in range(len(s)-1):

            print("number before ",number)
            print(f"CHECK roman[s[i]] {roman[s[i]] } < roman[s[(i+1)]] {roman[s[i+1]] }")
            if roman[s[i]] < roman[s[(i+1)]]:
                #print(f"roman[s[i]] {roman[s[i]] } < roman[s[(i+1)]] {roman[s[i+1]] }")
                number-=roman[s[i]]
                print("number after subtact",number)
            else:
                number+=roman[s[i]]
                print("number after add",number)
        print(f"number+roman[s[-1]] {number+roman[s[-1]]}")
        return number+roman[s[-1]]


if __name__ == "__main__":
  # s = "VIII" #testcase 1 > 8
  # s = "IXIX" #testcase 2 > 18
  # s  = "XIV" #testcase 3  > 14
  # s = "MCMXCIV"   #testcase 4 > 1994
   s = "CMXCIX" #testcase 5> 999
   obj1 = Solution()
   print("INPUT is ",s)
   result = obj1.romanToInt(s)
  
   print("RESUKLT",result)