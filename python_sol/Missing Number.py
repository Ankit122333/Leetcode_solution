class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        d = {}
        if len(nums) == 1:
            if nums[0] == 0:
                return 1
            else:
                return 0
        else:
            for i in range(len(nums)):
                d[nums[i]] = 2
            for i in range(len(d)):
                if i+1 in d:
                    continue
                else:
                    return i+1
            return 0