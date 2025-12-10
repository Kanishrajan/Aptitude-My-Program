# ------------------------------------------------------------
# Problem Title: Count Valid Unlock Permutations
# ------------------------------------------------------------
# Problem Description:
# You are given an array 'complexity' of length n.
# Computer 0 is already unlocked.
#
# Rule:
# A computer i can be unlocked using j if:
#     j < i   AND   complexity[j] < complexity[i]
#
# Find the number of valid permutations of [0..n-1] representing
# valid unlock orders. Return the result modulo 1e9+7.
#
# Example 1:
# Input:  complexity = [1,2,3]
# Output: 2
#
# Example 2:
# Input:  complexity = [3,3,3,4,4,4]
# Output: 0
# ------------------------------------------------------------
# Algorithm Used:
# 1. Check if every complexity[i] (i > 0) is strictly greater
#    than complexity[0]. If any is smaller or equal → impossible.
# 2. Otherwise, result = factorial(n-1), because after 0,
#    all other computers can be unlocked in any order.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# ------------------------------------------------------------

from typing import List

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        n = len(complexity)
        MOD = 10**9 + 7    
        c0 = complexity[0]
        for i in range(1, n):
            if complexity[i] <= c0:
                return 0
        res = 1
        for i in range(1, n):
            res = (res * i) % MOD
        return res


# ------------------------------------------------------------
# MAIN CLASS (Test Cases)
# ------------------------------------------------------------
if __name__ == "__main__":

    sol = Solution()

    # Test Case 1
    print("Test Case 1:")
    print(sol.countPermutations([1,2,3]))  # Expected: 2

    # Test Case 2
    print("\nTest Case 2:")
    print(sol.countPermutations([3,3,3,4,4,4]))  # Expected: 0

    # You can add more tests below:
    # print(sol.countPermutations([...]))
