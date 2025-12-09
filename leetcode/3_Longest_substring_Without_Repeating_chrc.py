"""
Problem: Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without duplicate characters.


Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. 
Note that "bca" and "cab" are also correct answers.


Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.


Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:
- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces.


Algorithm: Sliding Window with Hash Map
1. Use two pointers (left and right) to maintain a sliding window
2. Use a hash map to store the most recent index of each character
3. Expand the window by moving right pointer:
   - If current character is already in the window (exists in map and index >= left):
     * Move left pointer to (last occurrence index + 1)
   - Update the character's index in the map
   - Calculate current window length and update max_len
4. Return the maximum length found

Time Complexity: O(n) - where n is the length of string, we visit each character at most twice
Space Complexity: O(min(n, m)) - where m is the character set size (128 for ASCII)


Visual Example with "abcabcbb":
Step 1: left=0, right=0, char='a', window="a", len=1, max_len=1
Step 2: left=0, right=1, char='b', window="ab", len=2, max_len=2
Step 3: left=0, right=2, char='c', window="abc", len=3, max_len=3
Step 4: left=1, right=3, char='a', window="bca", len=3, max_len=3 (duplicate 'a', move left)
Step 5: left=2, right=4, char='b', window="cab", len=3, max_len=3 (duplicate 'b', move left)
Step 6: left=3, right=5, char='c', window="abc", len=3, max_len=3 (duplicate 'c', move left)
Step 7: left=6, right=6, char='b', window="b", len=1, max_len=3 (duplicate 'b', move left)
Step 8: left=6, right=7, char='b', window="b", len=1, max_len=3 (duplicate 'b', move left)
Result: max_len = 3
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Dictionary to store the most recent index of each character
        index_map = {}
        
        # Variables to track maximum length and left boundary of window
        max_len = 0
        left = 0
        
        # Iterate through the string with right pointer
        for right in range(len(s)):
            # If character is already in current window
            if s[right] in index_map and index_map[s[right]] >= left:
                # Move left pointer to skip the duplicate
                left = index_map[s[right]] + 1
            
            # Update the character's latest index
            index_map[s[right]] = right
            
            # Calculate current window length and update maximum
            max_len = max(max_len, right - left + 1)
        
        return max_len


# Main function for testing
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    s1 = "abcabcbb"
    print(f"Input: s = \"{s1}\"")
    print(f"Output: {solution.lengthOfLongestSubstring(s1)}")
    print(f"Expected: 3")
    print(f"Explanation: Longest substring is 'abc'\n")
    
    # Test Case 2
    s2 = "bbbbb"
    print(f"Input: s = \"{s2}\"")
    print(f"Output: {solution.lengthOfLongestSubstring(s2)}")
    print(f"Expected: 1")
    print(f"Explanation: Longest substring is 'b'\n")
    
    # Test Case 3
    s3 = "pwwkew"
    print(f"Input: s = \"{s3}\"")
    print(f"Output: {solution.lengthOfLongestSubstring(s3)}")
    print(f"Expected: 3")
    print(f"Explanation: Longest substring is 'wke'\n")
    
    # Test Case 4 - Empty string
    s4 = ""
    print(f"Input: s = \"{s4}\"")
    print(f"Output: {solution.lengthOfLongestSubstring(s4)}")
    print(f"Expected: 0")
    print(f"Explanation: Empty string has no characters\n")
    
    # Test Case 5 - Single character
    s5 = "a"
    print(f"Input: s = \"{s5}\"")
    print(f"Output: {solution.lengthOfLongestSubstring(s5)}")
    print(f"Expected: 1")
    print(f"Explanation: Single character is the longest\n")
    
    # Test Case 6 - All unique characters
    s6 = "abcdef"
    print(f"Input: s = \"{s6}\"")
    print(f"Output: {solution.lengthOfLongestSubstring(s6)}")
    print(f"Expected: 6")
    print(f"Explanation: All characters are unique\n")
    
    # Test Case 7 - With spaces and symbols
    s7 = "a b c a b c"
    print(f"Input: s = \"{s7}\"")
    print(f"Output: {solution.lengthOfLongestSubstring(s7)}")
    print(f"Expected: 4")
    print(f"Explanation: Longest substring is 'a b ' or ' b c'\n")
    
    # Test Case 8 - Complex case
    s8 = "dvdf"
    print(f"Input: s = \"{s8}\"")
    print(f"Output: {solution.lengthOfLongestSubstring(s8)}")
    print(f"Expected: 3")
    print(f"Explanation: Longest substring is 'vdf'")