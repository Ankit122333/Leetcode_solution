class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            n=abs(nums[i])
            nums[n-1]=-abs(nums[n-1])
        res=[]
        for j in range(len(nums)):
            if(nums[j]>0):
                res.append(j+1)
        return res

       