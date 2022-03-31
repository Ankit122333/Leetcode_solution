class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        C = collections.Counter(nums)
        res = []
        for k, v in C.items():
            if v == 1 and C[k-1] == 0 and C[k+1] == 0:
                res.append(k)
        return res