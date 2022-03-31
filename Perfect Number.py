class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num in set([6, 28, 496, 8128, 33550336, 8589869056]):
            return True
        else:
            return False
        