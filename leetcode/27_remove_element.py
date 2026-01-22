class Solution(object):
    def removeElement(self, nums, val):
        c = i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
                c += 1
                continue
            i += 1
        return len(nums)


# ---------------- TEST CASES ---------------- #

# Test Case 1: Normal case
nums = [3, 2, 2, 3]
val = 3
result = Solution().removeElement(nums, val)
print("Test Case 1 Output:", nums)
print("Length:", result)

# Test Case 2: No element to remove
nums = [1, 2, 3, 4]
val = 5
result = Solution().removeElement(nums, val)
print("Test Case 2 Output:", nums)
print("Length:", result)

# Test Case 3: All elements same as val
nums = [2, 2, 2, 2]
val = 2
result = Solution().removeElement(nums, val)
print("Test Case 3 Output:", nums)
print("Length:", result)

# Test Case 4: Mixed values
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
result = Solution().removeElement(nums, val)
print("Test Case 4 Output:", nums)
print("Length:", result)

# Test Case 5: Single element
nums = [1]
val = 1
result = Solution().removeElement(nums, val)
print("Test Case 5 Output:", nums)
print("Length:", result)