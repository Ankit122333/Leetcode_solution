class Solution:
    def twoSum(self, num, target):
        seen = {}
        for index, nums in enumerate(num):
            other = target - nums;
            if other in seen:
                return [seen[other], index]
            else:
                seen[nums] = index
        return []
        