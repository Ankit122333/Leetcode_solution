class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd=[]
        even=[]
        res=[]
        if(nums==0):
            return(res.append(0))
        for i in range(len(nums)):
            if(nums[i]%2==0):
                even.append(nums[i])
            else:
                odd.append(nums[i])
        res=even+odd
        '''for i in range(len(nums)//2):
            res.append(even[i])
        for i in range(len(nums)//2):
            res.append(odd[i])'''
        return res