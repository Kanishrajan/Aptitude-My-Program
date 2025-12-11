'''# Valid Word

## Problem Description

A word is considered valid if:
* It contains a minimum of 3 characters.
* It contains only digits (0-9), and English letters (uppercase and lowercase).
* It includes at least one vowel.
* It includes at least one consonant.

You are given a string `word`.

Return `true` if `word` is valid, otherwise, return `false`.

**Notes:**
* `'a'`, `'e'`, `'i'`, `'o'`, `'u'`, and their uppercases are vowels.
* A consonant is an English letter that is not a vowel.
Approach: Single Pass with Early Exit

1. **Initial Validation**
   - Check if word length is at least 3 characters
   - Verify all characters are alphanumeric (letters or digits only)
   - Return false immediately if either condition fails

2. **Character Classification**
   - Create a set of vowels (both uppercase and lowercase) for O(1) lookup
   - Initialize two boolean flags: `has_vowel` and `has_consonant`

3. **Single Pass Iteration**
   - Iterate through each character in the word
   - If character is a vowel, set `has_vowel = True`
   - If character is alphabetic but not a vowel, set `has_consonant = True`
   - **Optimization**: Return true immediately when both flags are true (early exit)

4. **Final Check**
   - After the loop, return true only if both vowel and consonant were found
'''
class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3 or not word.isalnum():
            return False
        
        vowels = set('aeiouAEIOU')
        has_vowel = has_consonant = False
        
        for ch in word:
            if ch in vowels:
                has_vowel = True
            elif ch.isalpha():
                has_consonant = True
            if has_vowel and has_consonant:
                return True
        
        return False


# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    word1 = "234Adas"
    print(f"Input: word = \"{word1}\"")
    print(f"Output: {solution.isValid(word1)}")
    print(f"Expected: True\n")
    
    # Example 2
    word2 = "b3"
    print(f"Input: word = \"{word2}\"")
    print(f"Output: {solution.isValid(word2)}")
    print(f"Expected: False\n")
    
    # Example 3
    word3 = "a3$e"
    print(f"Input: word = \"{word3}\"")
    print(f"Output: {solution.isValid(word3)}")
    print(f"Expected: False\n")
    
    # Additional test cases
    word4 = "123"
    print(f"Input: word = \"{word4}\"")
    print(f"Output: {solution.isValid(word4)}")
    print(f"Expected: False (no vowel/consonant)\n")
    
    word5 = "aaa"
    print(f"Input: word = \"{word5}\"")
    print(f"Output: {solution.isValid(word5)}")
    print(f"Expected: False (no consonant)\n")