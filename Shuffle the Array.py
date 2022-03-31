class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans=[]
        r = len(nums) // 2
        for l in range(len(nums) // 2):
            ans.append(nums[l])
            ans.append(nums[r])
            r += 1
        return ans