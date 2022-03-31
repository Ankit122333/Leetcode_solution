class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        r = num
        while r*r > num:
            r = (r + num//r) // 2
        if (r*r==num):
            return True
        else:
            return False
        