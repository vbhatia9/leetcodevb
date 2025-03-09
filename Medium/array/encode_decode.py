"""
Premium 271. Encode and Decode Strings
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]

Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.
"""

# The encode function iterates over the list of strings and concatenates the length of each string followed by a colon
# and the string itself. The decode function iterates over the encoded string and extracts the length of each string and the
# string itself. The length is used to extract the string from the encoded string, and the string is appended to the list of
# strings. The list of strings is then returned as the result.


class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string."""
        return "".join(f"{len(s)}:{s}" for s in strs)

    def decode(self, s):
        """Decodes a single string to a list of strings."""
        i = 0
        strs = []
        while i < len(s):
            j = s.find(":", i)  #finds the index of the colon
            length = int(s[i:j])    #extracts the length of the string
            i = j + 1 + length  #updates the index i
            strs.append(s[j + 1 : i])   #appends the string to the list
        return strs

#sol 2
class Codec2:
    def encode2(self, strs):
        """Encodes a list of strings to a single string."""
        
        new_str = ""
        for s in strs:
            new_str += str(len(s)) + "#" + s
            print(f"NEWSTR  {new_str}")
        return new_str
    

    def decode2(self, s):
        """Decodes a single string to a list of strings."""
        i = 0
        strs = []
        while i < len(s):
            j = s.find("#", i) # finds the index of the colon
            length = int(s[i:j]) #  extract the length of the string
            i = j + 1 + length #j is deliemiter so j+1 is the start of the string and length is the end of the string
            strs.append(s[j + 1 : i])   #appends the string to the list
        return strs


# Example usage:
codec = Codec()
encoded = codec.encode(["neet", "code", "love", "you"])
print(f"Encoded: {encoded}")
decoded = codec.decode(encoded)
print(f"Decoded: {decoded}")

codec2 = Codec2()
encoded2 = codec2.encode2(["neet", "code", "love", "you"])
print(f"Encoded2: {encoded2}")
decoded2 = codec2.decode2(encoded2)
print(f"Decoded2: {decoded2}")