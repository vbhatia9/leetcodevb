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


