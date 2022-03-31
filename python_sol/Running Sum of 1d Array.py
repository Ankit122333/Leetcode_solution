class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res=[]
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]
            res.append(sum)
        return res