class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(set(nums))<3: 
            return max(nums)
        nums.sort(reverse=True)
        count=1
        for i in range(len(nums)):
            if nums[i+1]!=nums[i]:
                count+=1
                if count==3:
                    return nums[i+1]