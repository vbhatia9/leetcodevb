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
        # print(f"{len(s), len(t)}")
        # if len(s)!= len(t):
        #  return False
        def nextValidChar(strng,indx):
            backspace= 0 
            while indx >= 0:
                print(f"Backpsace = {backspace} , strng[indx] = {strng[indx]}")
                if backspace == 0 and strng[indx] != '#':
                    break
                elif strng[indx] == '#':
                    backspace +=1
                else:
                     backspace -=1 # if no # backspace and backspace > 0 then decrement backspace
                
                indx-=1
            return indx

        s_index ,t_index  = len(s)-1,len(t)-1 # 2  pointer
        while s_index >=0 or t_index>=0: #IF anyone get <0 still it enters loop but will be return false below
        
            s_index = nextValidChar(s,s_index)
            t_index= nextValidChar(t,t_index)
        #check if the indx returned is out of range

            char_s = s[s_index] if s_index >=0 else ""
            char_t = t[t_index] if t_index >=0 else ""
            print(f"char_s = {char_s }  AND char_t = {char_t} ")
            if char_s != char_t:
                return False
            s_index-=1
            t_index-=1
        return True

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
    # s = "ab#c"
    # t = "ad#c"

    s= "bxj##tw"
    t = "bxj###tw"
    # s = "xywrrmp" 
    # t= "xywrrmu#p"
    obj1 = Solution()
    result = obj1.backspaceCompare(s,t)
    print(result)


