"""
345. Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.
 
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
 
Input: s = "IceCreAm"
 
Output: "AceCreIm"
 
Explanation:
 
The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".
 
 
Input: s = "custom"
Output: "costum"
"""
#sol1
# In this approach, we use two pointers, i and j, to iterate over the string s from the beginning and end, respectively.
# We check if the characters at positions i and j are vowels.
# If both characters are vowels, we swap them and increment i and decrement j.
# If the character at position i is not a vowel, we increment i.
# If the character at position j is not a vowel, we decrement j.
# We continue this process until i is less than j.
# Finally, we return the modified string s.
# This approach has a time complexity of O(n) since we iterate through the string s once.
# The space complexity is O(n) as we convert the string s to a list of characters.
# This approach is efficient and easy to implement.
def reverse_vowels(s):
    vowels = set('aeiouAEIOU')
    s = list(s)
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] not in vowels:
            i += 1
        elif s[j] not in vowels:
            j -= 1
        else:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
    return ''.join(s)


#sol2
"""

def reverse(s):
    n= len (s)
    lower_str= s.lower()
    vowels = ['a', 'e', 'i', 'o','u']
    pos_inx = []
    newoutput = ""
    for i,v in enumerate(lower_str):
           print(i,v)
           if v in vowels:
                pos_inx.append(i) #saving the index if its vowel


    print("pos_inx",pos_inx)     
    pos_inx.sort(reverse=True)
    print(pos_inx)
    
    # for indx in po
    # lower_str[p]
    
"""
if __name__ == "__main__":
    s = "IceCream"
    reverse_vowels(s)   #Output: "AceCrim"