class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        k=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[k]=nums[i]
                k+=1
        return k

# ---------------- TEST CASES ---------------- #
# Test Case 1: Normal case with duplicates
nums = [1, 1, 2]
result = Solution().removeDuplicates(nums)
print("Test Case 1 Output:", nums[:result])
# Expected Output: [1, 2]

# Test Case 2: No duplicates
nums = [1, 2, 3]
result = Solution().removeDuplicates(nums)
print("Test Case 2 Output:", nums[:result])
# Expected Output: [1, 2, 3]
# Test Case 3: All elements are the same
nums = [2, 2, 2, 2]
result = Solution().removeDuplicates(nums)
print("Test Case 3 Output:", nums[:result])
# Expected Output: [2]

# Test Case 4: Empty array
nums = []
result = Solution().removeDuplicates(nums)
print("Test Case 4 Output:", nums[:result])
# Expected Output: []

# Test Case 5: Large array with multiple duplicates
nums = [0,0,1,1,1,2,2,3,3,4]
result = Solution().removeDuplicates(nums)
print("Test Case 5 Output:", nums[:result])
# Expected Output: [0, 1, 2, 3, 4]
