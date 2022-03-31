class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        lst=[]
        for i in range(0,len(nums)):
            x=nums[i]
            count=0
            for j in range(0,len(nums)):
                if(j != i and nums[j] <x):
                    count+=1
            lst.append(count)
        return lst
        