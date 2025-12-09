# ------------------------------------------------------------
# Two Sum Problem (Description + Explanation + Code)
# ------------------------------------------------------------

# Problem Description:
# Given an array of integers nums and an integer target,
# return the indices of the two numbers such that they add up
# to the target.
#
# You may assume:
# - Exactly one valid solution exists.
# - You may not use the same element twice.
# - The answer can be returned in any order.
#
# Example 1:
# nums = [2,7,11,15], target = 9 → Output: [0,1]
#
# Example 2:
# nums = [3,2,4], target = 6 → Output: [1,2]
#
# Example 3:
# nums = [3,3], target = 6 → Output: [0,1]
#
# ------------------------------------------------------------
# Algorithm Explanation:
#
# This solution uses a hash map (dictionary) for fast lookups.
#
# Steps:
# 1. Create an empty dictionary numMap.
#    Key   → number
#    Value → index of that number
#
# 2. Loop through nums:
#       complement = target - nums[i]
#
#    Check if complement exists in numMap.
#    If yes → we found the pair, return indices.
#
# 3. Otherwise store nums[i] in map for future checks.
#
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# This is optimal. Brute force would take O(n²).
# ------------------------------------------------------------

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}  # number → index

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in numMap:
                return [numMap[complement], i]

            numMap[nums[i]] = i

        return []  # Not needed since problem guarantees one solution.


# ------------------------------------------------------------
# Main Function (You can run this directly)
# ------------------------------------------------------------

def main():
    print("Enter numbers separated by space:")
    nums = list(map(int, input().split()))

    print("Enter target value:")
    target = int(input())

    solver = Solution()
    result = solver.twoSum(nums, target)

    print("Indices of numbers adding to target:", result)


if __name__ == "__main__":
    main()
