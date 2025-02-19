
"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'

"""
class findbalanced():
   def find_brackets(self,inp):
        stk = [] #stack
        mapping = { ']':'[','}':'{',')':'('} #hash map
        for c in inp:
            if c in mapping:
                print(f"stk = {stk} stk[-1] = {stk[-1]} and c is {c}")
                if  stk and stk[-1] == mapping[c]:
                    print("STK popping",stk)
                    stk.pop()
                else: return False
            else:
                stk.append(c)
        print("STK final",stk)
        if stk:
            return False
        else: 
            return True

if __name__ == "__main__":
    inp = "()[]{}"
    
    obj1 = findbalanced()
    result = obj1.find_brackets(inp)
    print(" result", result)
    result = obj1.find_brackets("{]}")
    print(" result", result)