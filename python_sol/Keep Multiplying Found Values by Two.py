class Solution:
    def findFinalValue(self, nums: List[int], original: int):
        '''for i in range(len(nums)):
            if(nums[i]==original):
                i=0
                original *= 2'''
        while original in nums:
            original*=2
        return original