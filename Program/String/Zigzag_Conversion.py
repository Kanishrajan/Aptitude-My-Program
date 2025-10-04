class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        rows = ["" for _ in range(numRows)]
        cur, down = 0, -1
        for c in s:
            rows[cur] += c
            if cur == 0 or cur == numRows - 1:
                down *= -1   
            cur += down
        return "".join(rows)
solution = Solution()
print(solution.convert("PAYPALISHIRING", 3)) 
print(solution.convert("PAYPALISHIRING", 4))  
print(solution.convert("A", 1))               
