'''class Solution:
    def findGCD(self, nums: List[int]) -> int:
        x=sorted(nums)
        return math.gcd(nums[0],nums[-1])'''
from math import gcd
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        return gcd(max(nums),min(nums))