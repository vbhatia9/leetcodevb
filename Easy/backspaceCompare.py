"""
844. Backspace String Compare
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
 

Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.
 
"""
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def nextValidChar(strng,indx):
            backspace= 0 
            while indx > 0:

                if backspace == 0 and strng[indx] != '#':
                    break
                elif strng[indx] == '#':
                    backspace +=1
                else:
                    indx-=1
            return indx

        s_index = nextValidChar(s,len(s))
        t_index = nextValidChar(t,len(t))
        #check if the indx returned is out of range

        if s_index != t_index:
            return False


        #Sol 2
        # stk= []
        # if len(s)!=len(t):
        #     return False
        # for c in s:
        #      #Check the length of stack first and then see the last element inserted it equal to c or not
        #     if   len(stk)>0 and c == "*":  
        #         print(f"stk before pop = {stk}  ")
        #         stk.pop()
        #         print(f"stk AFTER pop = {stk} ")
        #     else:
        #         stk.append(c)
        #         print(f"stk after append{stk} ")
        # newstk= ''.join(stk)



if __name__ == "__main__": 
    s = "ab#c", t = "ad#c"
    obj1 = Solution()
    result = obj1.backspaceCompare(s,t)


