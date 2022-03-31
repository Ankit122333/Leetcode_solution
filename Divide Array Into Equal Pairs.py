from itertools import compress
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        res = len(nums)
        count = sum(num//2 for num in Counter(nums).values())
        return (res/2 == count)