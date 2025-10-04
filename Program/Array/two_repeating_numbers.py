class Solution:
    def twoRepeated(self, arr):
        seen = set()
        res = []
        for num in arr:
            if num in seen:          
                res.append(num)
                if len(res) == 2:   
                    return res
            else:
                seen.add(num)
arr = [1, 2, 1, 3, 4, 3]
n = 4
print(Solution().twoRepeated(arr))