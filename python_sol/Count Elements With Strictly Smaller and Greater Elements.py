class Solution:
    def countElements(self, nums: List[int]) -> int:
        p=len(nums)
        maxm=max(nums)
        minm=min(nums)
        c=0
        for x in nums:
            if x>minm and x<maxm:
                c+=1
        return c