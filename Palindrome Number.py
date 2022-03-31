class Solution:
    def isPalindrome(self, x: int) -> bool:
        dividend = x 
        remainder = dividend % 10
        Previous_remainder = 0
        while  dividend > 0:
            Previous_remainder = (Previous_remainder * 10) + remainder 
            dividend = dividend // 10 
            remainder = dividend % 10 
        return (Previous_remainder == x)