"""

1047. Remove All Adjacent Duplicates In String
You are given a string s consisting of lowercase English letters. 
A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

 

Example 1:

Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".

Example 2:

Input: s = "azxxzy"
Output: "ay"
 
"""
#Solution 1
# In this approach, we use a stack to store the characters of the input string s.
# We iterate through each character in s and compare it with the top element of the stack.
# If the character is equal to the top element, we pop the top element from the stack.
# Otherwise, we push the character onto the stack.
# Finally, we join the characters in the stack to form the final string.
# This approach has a time complexity of O(n) since we iterate through each character in s once.
# The space complexity is also O(n) to store the characters in the stack.
# This approach is efficient and easy to implement.
class Removedup:
    def removeDuplicates(self, s: str) -> str:
        stk= []
        for c in s:
             #Check the length of stack first and then see the last element inserted it equal to c or not
            if   len(stk)>0 and c in stk[-1]: 
                print(f"c = {c} , stk before pop = {stk}  ")
                stk.pop()
                print(f"c = {c} , stk AFTER pop = {stk} ")
            else:
                 
                stk.append(c)
                print(f"stk after append{stk} and c is {c}")
        newstk= ''.join(stk)
        print(newstk)
        return newstk


if __name__ == "__main__": 
    s= "aababaab"
    obj1 = Removedup()
    result = obj1.removeDuplicates(s)


