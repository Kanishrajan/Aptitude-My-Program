"""
Problem: Special Triplets

You are given an integer array nums.

A special triplet is defined as a triplet of indices (i, j, k) such that:
- 0 <= i < j < k < n, where n = nums.length
- nums[i] == nums[j] * 2
- nums[k] == nums[j] * 2

Return the total number of special triplets in the array.
Since the answer may be large, return it modulo 10^9 + 7.


Example 1:
Input: nums = [6,3,6]
Output: 1
Explanation:
The only special triplet is (i, j, k) = (0, 1, 2), where:
- nums[0] = 6, nums[1] = 3, nums[2] = 6
- nums[0] = nums[1] * 2 = 3 * 2 = 6
- nums[2] = nums[1] * 2 = 3 * 2 = 6


Example 2:
Input: nums = [0,1,0,0]
Output: 1
Explanation:
The only special triplet is (i, j, k) = (0, 2, 3), where:
- nums[0] = 0, nums[2] = 0, nums[3] = 0
- nums[0] = nums[2] * 2 = 0 * 2 = 0
- nums[3] = nums[2] * 2 = 0 * 2 = 0


Example 3:
Input: nums = [8,4,2,8,4]
Output: 2
Explanation:
There are exactly two special triplets:
1. (i, j, k) = (0, 1, 3)
   - nums[0] = 8, nums[1] = 4, nums[3] = 8
   - nums[0] = nums[1] * 2 = 4 * 2 = 8
   - nums[3] = nums[1] * 2 = 4 * 2 = 8
2. (i, j, k) = (1, 2, 4)
   - nums[1] = 4, nums[2] = 2, nums[4] = 4
   - nums[1] = nums[2] * 2 = 2 * 2 = 4
   - nums[4] = nums[2] * 2 = 2 * 2 = 4


Constraints:
- 3 <= n == nums.length <= 10^5
- 0 <= nums[i] <= 10^5


Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List
from collections import Counter

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        
        freq_prev = Counter()
        freq_next = Counter(nums)
        ans = 0
        
        for num in nums:
            freq_next[num] -= 1
            ans += freq_prev[num * 2] * freq_next[num * 2]
            freq_prev[num] += 1
        
        return ans % MOD


# Main function for testing
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    nums1 = [6, 3, 6]
    print(f"Input: {nums1}")
    print(f"Output: {solution.specialTriplets(nums1)}")
    print(f"Expected: 1\n")
    
    # Test Case 2
    nums2 = [0, 1, 0, 0]
    print(f"Input: {nums2}")
    print(f"Output: {solution.specialTriplets(nums2)}")
    print(f"Expected: 1\n")
    
    # Test Case 3
    nums3 = [8, 4, 2, 8, 4]
    print(f"Input: {nums3}")
    print(f"Output: {solution.specialTriplets(nums3)}")
    print(f"Expected: 2\n")
    
    # Test Case 4 - Edge case with larger array
    nums4 = [10, 5, 10, 5, 10]
    print(f"Input: {nums4}")
    print(f"Output: {solution.specialTriplets(nums4)}")
    print(f"Expected: 4\n")
    
    # Test Case 5 - All same numbers
    nums5 = [4, 2, 4, 2, 4]
    print(f"Input: {nums5}")
    print(f"Output: {solution.specialTriplets(nums5)}")
    print(f"Expected: 2")