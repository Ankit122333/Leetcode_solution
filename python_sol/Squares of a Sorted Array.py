class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        lst=[]
        for i in range(0,len(nums)):
            x=nums[i]*nums[i]
            lst.append(x)
        return sorted(lst)