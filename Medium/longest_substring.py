"""

3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 
"""

def length_of_longest_substring(s: str) -> int:
    char_index_map = {}
    longest = 0
    start = 0

    for i, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start:    # Check if the character is already in the substring
            start = char_index_map[char] + 1 # Move the start index to the right of the last occurrence of the character
        char_index_map[char] = i # Update the last occurrence of the character
        longest = max(longest, i - start + 1) # Update the longest substring length

    return longest

# Example usage:
if __name__ == "__main__":
    s = "abcabcbb"
    print(length_of_longest_substring(s))  # Output: 3
    s = "bbbbb"
    print(length_of_longest_substring(s))  # Output: 1
    s = "pwwkew"
    print(length_of_longest_substring(s))  # Output: 3
    s = ""
    print(length_of_longest_substring(s))  # Output: 0