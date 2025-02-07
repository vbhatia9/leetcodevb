"""242. Valid Anagram
Given two strings s and t, return true if t is an
anagram
of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 """

from collections import Counter

def valid_anagram(s:str,target:str):
    #sol 1
    #print(f"Sorted S {sorted(s)} ,sorted T {sorted(target)}")
    # if sorted(s) == sorted(target):
    #     return True
   
    # return False

    #sol 2
    if Counter(s)== Counter(target):
        return True
   
    return False

    #sol 3



if __name__ == "__main__":
    s = "anagram" 
    t = "nagaram"
    #s = "rat"
    #t = "car"
    print(valid_anagram(s,t))