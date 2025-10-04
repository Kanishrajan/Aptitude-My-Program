class Solution:
    def findExtra(self, arr1, arr2):
        lo, hi = 0, len(arr1) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if mid >= len(arr2) or arr1[mid] != arr2[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo
arr1 = [433,483,577,685,800,850,940]
arr2 = [433,483,577,685,800,850]
print(Solution().findExtra(arr1, arr2))