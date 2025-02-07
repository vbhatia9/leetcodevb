# Given a string s, reverse only all the vowels in the string and return it.
 
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
 
# Input: s = "IceCreAm"
 
# Output: "AceCreIm"
 
# Explanation:
 
# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".
 
 
# Input: s = "custom"
# Output: "costum"

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
    

if __name__ == "__main__":
    s = "IceCream"
    reverse(s)