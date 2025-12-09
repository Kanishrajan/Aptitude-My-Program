"""
Problem: Zigzag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows.


Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Explanation:
P   A   H   N
A P L S I I G
Y   I   R


Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I


Example 3:
Input: s = "A", numRows = 1
Output: "A"


Constraints:
- 1 <= s.length <= 1000
- s consists of English letters (lower-case and upper-case), ',' and '.'
- 1 <= numRows <= 1000


Algorithm: Simulate Zigzag Pattern
1. Handle edge cases:
   - If numRows is 1 or numRows >= string length, return original string
   
2. Create an array of empty strings for each row
   
3. Use two variables:
   - cur: current row index (starts at 0)
   - down: direction indicator (1 for down, -1 for up)
   
4. Iterate through each character in the string:
   - Add character to the current row
   - If at top row (cur == 0) or bottom row (cur == numRows - 1):
     * Reverse direction (multiply down by -1)
   - Move to next row (cur += down)
   
5. Join all rows together and return the result


Time Complexity: O(n) - where n is the length of string, we visit each character once
Space Complexity: O(n) - to store the result in rows array


Visual Example with "PAYPALISHIRING", numRows = 3:

Initial state:
rows = ["", "", ""]
cur = 0, down = -1

Step-by-step:
Char 'P': rows[0] += 'P' → ["P", "", ""], cur=0 (at top), down=1, cur=1
Char 'A': rows[1] += 'A' → ["P", "A", ""], cur=1, down=1, cur=2
Char 'Y': rows[2] += 'Y' → ["P", "A", "Y"], cur=2 (at bottom), down=-1, cur=1
Char 'P': rows[1] += 'P' → ["P", "AP", "Y"], cur=1, down=-1, cur=0
Char 'A': rows[0] += 'A' → ["PA", "AP", "Y"], cur=0 (at top), down=1, cur=1
Char 'L': rows[1] += 'L' → ["PA", "APL", "Y"], cur=1, down=1, cur=2
Char 'I': rows[2] += 'I' → ["PA", "APL", "YI"], cur=2 (at bottom), down=-1, cur=1
Char 'S': rows[1] += 'S' → ["PA", "APLS", "YI"], cur=1, down=-1, cur=0
Char 'H': rows[0] += 'H' → ["PAH", "APLS", "YI"], cur=0 (at top), down=1, cur=1
Char 'I': rows[1] += 'I' → ["PAH", "APLSI", "YI"], cur=1, down=1, cur=2
Char 'R': rows[2] += 'R' → ["PAH", "APLSI", "YIR"], cur=2 (at bottom), down=-1, cur=1
Char 'I': rows[1] += 'I' → ["PAH", "APLSII", "YIR"], cur=1, down=-1, cur=0
Char 'N': rows[0] += 'N' → ["PAHN", "APLSII", "YIR"], cur=0 (at top), down=1, cur=1
Char 'G': rows[1] += 'G' → ["PAHN", "APLSIIG", "YIR"], cur=1, down=1, cur=2

Final: join(["PAHN", "APLSIIG", "YIR"]) = "PAHNAPLSIIGYIR"
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge cases: if only 1 row or numRows >= string length, no zigzag needed
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create an array to store characters for each row
        rows = ["" for _ in range(numRows)]
        
        # cur: current row index, down: direction (-1 for up, 1 for down)
        cur = 0
        down = -1
        
        # Iterate through each character in the string
        for c in s:
            # Add current character to the current row
            rows[cur] += c
            
            # If at top or bottom row, reverse direction
            if cur == 0 or cur == numRows - 1:
                down *= -1
            
            # Move to next row based on direction
            cur += down
        
        # Join all rows together to get the final result
        return "".join(rows)


# Main function for testing
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    s1 = "PAYPALISHIRING"
    numRows1 = 3
    print(f"Input: s = \"{s1}\", numRows = {numRows1}")
    print(f"Output: {solution.convert(s1, numRows1)}")
    print(f"Expected: PAHNAPLSIIGYIR")
    print("Pattern:")
    print("P   A   H   N")
    print("A P L S I I G")
    print("Y   I   R\n")
    
    # Test Case 2
    s2 = "PAYPALISHIRING"
    numRows2 = 4
    print(f"Input: s = \"{s2}\", numRows = {numRows2}")
    print(f"Output: {solution.convert(s2, numRows2)}")
    print(f"Expected: PINALSIGYAHRPI")
    print("Pattern:")
    print("P     I    N")
    print("A   L S  I G")
    print("Y A   H R")
    print("P     I\n")
    
    # Test Case 3
    s3 = "A"
    numRows3 = 1
    print(f"Input: s = \"{s3}\", numRows = {numRows3}")
    print(f"Output: {solution.convert(s3, numRows3)}")
    print(f"Expected: A\n")
    
    # Test Case 4 - Two rows
    s4 = "ABCDEFGH"
    numRows4 = 2
    print(f"Input: s = \"{s4}\", numRows = {numRows4}")
    print(f"Output: {solution.convert(s4, numRows4)}")
    print(f"Expected: ACEGBDFH")
    print("Pattern:")
    print("A C E G")
    print("B D F H\n")
    
    # Test Case 5 - Single character with multiple rows
    s5 = "A"
    numRows5 = 5
    print(f"Input: s = \"{s5}\", numRows = {numRows5}")
    print(f"Output: {solution.convert(s5, numRows5)}")
    print(f"Expected: A\n")
    
    # Test Case 6 - Five rows
    s6 = "ABCDEFGHIJKLMNO"
    numRows6 = 5
    print(f"Input: s = \"{s6}\", numRows = {numRows6}")
    print(f"Output: {solution.convert(s6, numRows6)}")
    print(f"Expected: AIGBHJCFKDELN")
    print("Pattern:")
    print("A       I")
    print("B     H J")
    print("C   G   K")
    print("D F     L N")
    print("E       M O\n")
    
    # Test Case 7 - String with special characters
    s7 = "A,B.C"
    numRows7 = 2
    print(f"Input: s = \"{s7}\", numRows = {numRows7}")
    print(f"Output: {solution.convert(s7, numRows7)}")
    print(f"Expected: A.CB,")