class Solution(object):
    def merge(self, nums1, m, nums2, n):
        for j in range(n):
            nums1[m + j] = nums2[j]
        nums1.sort()


# ---------------- TEST CASES ---------------- #

# Test Case 1
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
Solution().merge(nums1, m, nums2, n)
print("Test Case 1 Output:", nums1)

# Test Case 2
nums1 = [1, 2, 3]
m = 3
nums2 = []
n = 0
Solution().merge(nums1, m, nums2, n)
print("Test Case 2 Output:", nums1)

# Test Case 3
nums1 = [0, 0, 0]
m = 0
nums2 = [2, 5, 6]
n = 3
Solution().merge(nums1, m, nums2, n)
print("Test Case 3 Output:", nums1)

# Test Case 4
nums1 = [4, 5, 6, 0, 0, 0]
m = 3
nums2 = [1, 2, 3]
n = 3
Solution().merge(nums1, m, nums2, n)
print("Test Case 4 Output:", nums1)

# Test Case 5
nums1 = [-3, -1, 0, 0, 0]
m = 2
nums2 = [-2, 4, 5]
n = 3
Solution().merge(nums1, m, nums2, n)
print("Test Case 5 Output:", nums1)